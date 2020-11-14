"""used to generate the order number"""
import uuid 


from django.db import models
"""built in django model to help calculate costs"""
from django.db.models import Sum 
"""settings.py file"""
from django.conf import settings 
"""OrderLineItem has foreign key to it so need to import it"""
from products.models import Product 

""" Order model will handle all orders accross the store"""
class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    """ null=true because not every country has postcode"""
    postcode = models.CharField(max_length=20, null=True, blank=True) 
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    """ null=true because not every country has county"""
    county = models.CharField(max_length=80, null=True, blank=True) 
    """ auto_now_add will automatically set date and time """
    date = models.DateTimeField(auto_now_add=True) 
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def _generate_order_number(self): 
        """starts with an underscore to tell django that it is a private method that will
        only be used inside this class. It will generate a random, unique order number using UUID"""
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum']
        """using the sum function across all the line-item total fields for all line items on this order."""
        """taken from the settings file to calculate delivery"""
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD: 
            self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number

""" related to the Order model. A line item will be like an individual shopping bag related to a specific order
and referencing the product itself.
Idea here is that when the user checkouts, the information they put in the order from will be used to create an order 
instance. And then we'll iterate through the items in the shopping bag.
Creating an order line item for each one. Attaching it to the order.
And updating the delivery cost, order total, and grand total along the way.
"""
class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    product_size = models.CharField(max_length=2, null=True, blank=True) # XS, S, M, L, XL
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'
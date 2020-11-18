"""This is the way to update the order total, delivery cost, and grand_total for each order
as users add line items to it.
The basic process is that will first create an order. Then iterate through the shopping bag.
And add line items to it one by one updating the various costs along the way.
The method to update the total is already in the order model.
We just need a way to call it each time a line item is attached to the order.
To accomplish this we'll use a built-in feature of django called signals.
"""

from django.db.models.signals import post_save, post_delete
""" post means after. So this implies these signals are sent by django to the entire application
after a model instance is saved and after it's deleted respectively."""
from django.dispatch import receiver

from .models import OrderLineItem

"""receiver decorator to tell django we are recieving post_save signals frrom the OrderLineItem model"""
@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    instance.order.update_total()

@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    instance.order.update_total()
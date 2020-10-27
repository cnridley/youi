from django.shortcuts import render
from .models import Product

# Create your views here.

def all_products(request):
    """A view to show all products selling"""
    product = Product.objects.all()

    context = {
        'product': product,
    }

    return render(request, 'products.html', context)
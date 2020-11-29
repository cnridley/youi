from django.shortcuts import render
from .models import Product
from Profile.models import Profile

# Create your views here.

def all_products(request):
    """A view to show all products selling"""
    products = Product.objects.all()
    user = Profile.objects.all()

    context = {
        'products': products,
        'user': user
    }

    return render(request, 'products.html', context)

    
   
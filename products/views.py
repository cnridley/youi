from django.shortcuts import render, reverse, redirect
from .models import Product
from Profile.models import Profile
from .forms import ProductForm

# Create your views here.

def all_products(request):
    """A view to show all products selling"""
    products = Product.objects.all()
    user = Profile.objects.all()

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('all_products'))
        
    else:
        form = ProductForm()

    context = {
        'products': products,
        'user': user,
        'form': form,
    }

    return render(request, 'products.html', context)

    
   
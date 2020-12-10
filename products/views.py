from django.shortcuts import render, reverse, redirect, get_object_or_404
from .models import Product
from Profile.models import Profile
from .forms import ProductForm
from django.contrib import messages

# Create your views here.

def all_products(request):
    """A view to show all products selling"""
    products = Product.objects.all()
    user = Profile.objects.all()

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('products'))
        
    else:
        form = ProductForm()

    context = {
        'products': products,
        'user': user,
        'form': form,
    }

    return render(request, 'products.html', context)

def edit_product(request, product_id):
    """ Edit a product in the store """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.info(request, 'Successfully updated product!')
            return redirect(reverse('products'))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)
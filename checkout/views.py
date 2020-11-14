from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    """retrieve bag from current session"""
    bag = request.session.get('bag', {})
    """if nothing in the bag return an error message and re-direct to products page"""
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    """create an instance of order form"""
    order_form = OrderForm()
    template = 'checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)
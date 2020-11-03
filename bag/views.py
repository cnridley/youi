from django.shortcuts import render

# Create your views here.

def shopping_bag(request):
    """A view to show all products selling"""
    return render(request, 'bag.html')
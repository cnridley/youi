from django.shortcuts import render

# Create your views here.
def Profile(request):
    """A view to return profile page"""
    
    template = 'Profile.html'

    context = {}

    return render(request, template, context)
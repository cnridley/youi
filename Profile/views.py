from django.shortcuts import render
from .models import Profile

# Create your views here.
def get_profile(request):
    """A view to return profile page"""
    user = Profile.objects.all()

    template = 'Profile.html'

    context = {
        'user': user,
    }


    return render(request, template, context)
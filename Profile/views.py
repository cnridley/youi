from django.shortcuts import render
from .models import Profile

def profile(request):
    """ Display the user's profile. """
    user = Profile.objects.all()
    template = 'Profile.html'
    context = {
        'user': user
    }

    return render(request, template, context)
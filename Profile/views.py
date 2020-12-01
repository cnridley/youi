from django.shortcuts import render, reverse
from .models import Profile
from workouts.forms import WorkoutForm
from workouts.models import workouts
from workouts.views import workouts_page

def profile(request):
    """ Display the user's profile. """
    user = Profile.objects.all()
    template = 'Profile.html'
    context = {
        'user': user,
    }

    return render(request, template, context)
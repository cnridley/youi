from django.shortcuts import render, reverse, redirect
from .models import ProgressionPicture
from Profile.models import Profile

# Create your views here.

def progression_pictures(request):
    user = Profile.objects.all()

    context = {
        'user': user,
    }

    template = 'progression_pics.html'

    return render(request, template, context)

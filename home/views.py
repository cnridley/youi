from django.shortcuts import render
from Profile.models import Profile
# Create your views here.

def index(request):
    """A view to return index page"""
    user = Profile.objects.all()
    context = {
        'user': user
    }

    return render(request, 'index.html', context)

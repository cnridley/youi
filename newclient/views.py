from django.shortcuts import render
from Profile.models import Profile
# Create your views here.

def newclient(request):
    """A view to return index page"""
    user = Profile.objects.all()
    context = {
        'user': user
    }

    return render(request, 'newclient.html', context)

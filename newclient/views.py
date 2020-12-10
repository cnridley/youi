from django.shortcuts import render, redirect
from Profile.models import Profile
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
# Create your views here.

def newclient(request):
    """A view to return index page"""
    user = Profile.objects.filter(user=request.user)

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal)
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    
    context = {
        'user': user,
        'form': form,
    }

    return render(request, 'newclient.html', context)

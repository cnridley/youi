from django.shortcuts import render, reverse, redirect
from .models import ProgressionPicture
from Profile.models import Profile
from .forms import ProgressionForm

# Create your views here.

def progression_pictures(request):
    user = Profile.objects.all()
    progression = ProgressionPicture.objects.all()
    
    if request.method == 'POST':
        form = ProgressionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('progression_pictures'))
    else:
        form = ProgressionForm()

    context = {
        'user': user,
        'progression': progression,
        'form': form
    }

    template = 'progression_pics.html'

    return render(request, template, context)

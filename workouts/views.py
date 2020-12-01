from django.shortcuts import render, reverse, redirect
from .forms import WorkoutForm
from Profile.models import Profile
from .models import workouts

# Create your views here.

def workouts_page(request):
    user = Profile.objects.all()
    workout = workouts.objects.all()

    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('workouts_page'))
    else:
        form = WorkoutForm()

    context = {
        'user': user,
        'workout': workout,
        'form': form,
    }
    
    template = 'workouts.html'

    return render(request, template, context)
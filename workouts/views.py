from django.shortcuts import render, reverse, redirect, get_object_or_404
from .forms import WorkoutForm
from Profile.models import Profile
from .models import workouts
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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

@login_required
def edit_workout(request, workout_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.info(request, 'Sorry, you can not do that.')
        return redirect(reverse('Profile'))

    workout = get_object_or_404(workouts, pk=workout_id)
    if request.method == 'POST':
        form = WorkoutForm(request.POST, request.FILES, instance=workout)
        if form.is_valid():
            form.save()
            messages.info(request, 'Successfully updated workout!')
            return redirect(reverse('workouts_page'))
        else:
            messages.error(request, 'Failed to update picture. Please ensure the form is valid.')
    else:
        form = WorkoutForm(instance=workout)

    template = 'edit_workout.html'
    
    context = {
        'form': form,
        'workout': workout,
    }

    return render(request, template, context)

@login_required
def delete_workout(request, workouts_id):
    """ Delete a product from the store """
    if not request.user.is_authenticated:
        messages.info(request, 'Sorry, you can not do that!')
        return redirect(reverse('workouts'))

    picture = get_object_or_404(workouts, pk=workouts_id)
    picture.delete()
    messages.info(request, 'Picture deleted!')
    return redirect(reverse('workouts_page'))
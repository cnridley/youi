from django.shortcuts import render, reverse, redirect, get_object_or_404
from .models import ProgressionPicture
from Profile.models import Profile
from .forms import ProgressionForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def progression_pictures(request):
    user = Profile.objects.all()
    progression = ProgressionPicture.objects.all()
    
    if request.method == 'POST':
        form = ProgressionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('progression_pictures'))
    else:
        form = ProgressionForm()

    context = {
        'user': user,
        'progression': progression,
        'form': form,
    }

    return render(request, 'progression_pics.html', context)

@login_required
def delete_picture(request, progressionpicture_id):
    """ Delete a product from the store """
    if not request.user.is_authenticated:
        messages.info(request, 'Sorry, you can not do that!')
        return redirect(reverse('Profile'))

    picture = get_object_or_404(ProgressionPicture, pk=progressionpicture_id)
    picture.delete()
    messages.info(request, 'Picture deleted!')
    return redirect(reverse('progression_pictures'))

@login_required
def edit_picture(request, progression_id):
    """ Edit a product in the store """
    if not request.user.is_authenticated:
        messages.info(request, 'Sorry, you can not do that.')
        return redirect(reverse('Profile'))

    progression = get_object_or_404(ProgressionPicture, pk=progression_id)
    if request.method == 'POST':
        form = ProgressionForm(request.POST, request.FILES, instance=progression)
        if form.is_valid():
            form.save()
            messages.info(request, 'Successfully updated picture!')
            return redirect(reverse('progression_pictures'))
        else:
            messages.error(request, 'Failed to update picture. Please ensure the form is valid.')
    else:
        form = ProgressionForm(instance=progression)

    template = 'edit_picture.html'
    
    context = {
        'form': form,
        'progression': progression,
    }

    return render(request, template, context)

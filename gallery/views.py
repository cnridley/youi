from django.shortcuts import render, reverse, redirect
from .models import Gallery
from .forms import ImageForm
from Profile.models import Profile
# Create your views here.

def gallery(request):
    """A view to return gallery page"""
    gallery = Gallery.objects.all()
    user = Profile.objects.all()
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('gallery'))
    else:
        form = ImageForm()

    context = {
        'gallery': gallery,
        'form': form,
        'user': user,
    }

    return render(request, 'gallery.html', context)




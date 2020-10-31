from django.shortcuts import render, reverse, redirect
from .models import Gallery
from .forms import ImageForm

# Create your views here.

def gallery(request):
    """A view to return gallery page"""
    gallery = Gallery.objects.all()
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('gallery'))
    else:
        form = ImageForm()

    context = {
        'gallery': gallery,
        'form': form
    }

    return render(request, 'gallery.html', context)




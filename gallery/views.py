from django.shortcuts import render
from .models import Gallery
from .forms import ImageForm

# Create your views here.

def gallery(request):
    """A view to return gallery page"""
    gallery = Gallery.objects.all()

    context = {
        'gallery': gallery,
    }

    return render(request, 'gallery.html', context)

def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'gallery.html', {'form': form})
    else:
        form = ImageForm()
    return render(request, 'gallery.html', {'form': form})


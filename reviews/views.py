from django.shortcuts import render, reverse, redirect
from .models import Reviews
from Profile.models import Profile
from .forms import ReviewForm

# Create your views here.
def reviews(request):
    review = Reviews.objects.all()
    user = Profile.objects.all()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('reviews'))
    else:
        form = ReviewForm()

    context = {
        'review': review,
        'user': user,
        'form': form,
    }

    return render(request, 'reviews.html', context)
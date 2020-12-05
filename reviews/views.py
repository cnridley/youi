from django.shortcuts import render
from .models import Reviews
from Profile.models import Profile

# Create your views here.

def reviews(request):
    review = Reviews.objects.all()
    user = Profile.objects.all()

    context = {
        'review' : review,
        'user': user,
    }

    return render(request, 'reviews.html', context)
from django.shortcuts import render, reverse, redirect, get_object_or_404
from .models import Reviews
from Profile.models import Profile
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required

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

@login_required
def delete_review(request, reviews_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.info(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Reviews, pk=reviews_id)
    product.delete()
    messages.success(request, 'Review deleted!')
    return redirect(reverse('reviews'))

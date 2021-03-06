from django.shortcuts import render, reverse, redirect
from Profile.models import Profile
from .forms import CommentForm
from .models import comment
from Profile.views import profile

# Create your views here.

def comments(request):
    user = Profile.objects.filter(user=request.user)
    user_comment = comment.objects.filter(user=request.user)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('comments'))
    else:
        form = CommentForm()

    context = {
        'user': user,
        'user_comment': user_comment,
        'form': form,
    }

    return render(request, 'comments.html', context)

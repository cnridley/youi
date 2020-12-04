from django.shortcuts import render

# Create your views here.

def comments(request):
    context ={}

    return render(request, 'comments.html', context)

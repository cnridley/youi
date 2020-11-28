from django.shortcuts import render


def profile(request):
    """ Display the user's profile. """

    template = 'Profiles.html'
    context = {}

    return render(request, template, context)
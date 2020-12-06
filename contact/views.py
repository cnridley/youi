from django.shortcuts import render, redirect, reverse
from Profile.models import Profile
from django.http import HttpResponse
from .forms import ContactForm 
from django.core.mail import send_mail
from home.views import index
# Create your views here.

def contact(request):
    """A view to return index page"""
    user = Profile.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # send email code goes here
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']
            message = "{0} has sent you a new message:\n\n{1}".format(sender_name, form.cleaned_data['message'])
            send_mail('New Enquiry', message, sender_email, ['cnridley1@gmail.com'])
            return redirect(reverse(contact))
        
    else:
        form = ContactForm()

    context = {
        'user': user,
        'form': form,
    }

    return render(request, 'contact.html', context)

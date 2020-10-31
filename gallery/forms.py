from django import forms
from .models import Gallery

class ImageForm(forms.ModelForm):
    """form for the Gallery model"""
    class Meta():
        model = Gallery
        fields = ('name', 'image')
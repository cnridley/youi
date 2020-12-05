from django import forms
from .models import Reviews

class ReviewForm(forms.ModelForm):
    """form for the comment model"""
    class Meta():
        model = Reviews
        fields = ('name', 'title', 'rating', 'text')
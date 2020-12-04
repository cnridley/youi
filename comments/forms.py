from django import forms
from .models import comment

class CommentForm(forms.ModelForm):
    """form for the comment model"""
    class Meta():
        model = comment
        fields = ('title', 'text')
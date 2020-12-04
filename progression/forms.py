from django import forms
from .models import ProgressionPicture

class ProgressionForm(forms.ModelForm):
    class Meta():
        model = ProgressionPicture
        fields = ('user', 'week', 'progression_pic', 'chest_measurement', 'waist_measurement', 'weight')
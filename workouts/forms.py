from django import forms
from .models import workouts

class WorkoutForm(forms.ModelForm):
    """form for the workouts model"""
    class Meta():
        model = workouts
        fields = ('user', 'weeks', 'body_part', 'exercise1', 'sets1', 'reps1',
        'exercise2', 'sets2', 'reps2',
        'exercise3', 'sets3', 'reps3',
        'exercise4', 'sets4', 'reps4',
        'exercise5', 'sets5', 'reps5',
        'exercise6', 'sets6', 'reps6',
        'exercise7', 'sets7', 'reps7',
        'exercise8', 'sets8', 'reps8',
        'exercise9', 'sets9', 'reps9',
        'exercise10', 'sets10', 'reps10',
        'gym_or_home')
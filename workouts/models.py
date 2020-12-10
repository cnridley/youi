from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from Profile.models import Profile

# Create your models here.

class workouts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    weeks = models.CharField(max_length=250, null=True, blank=True)
    body_part = models.CharField(max_length=250, null=True, blank=True)
    exercise1 = models.CharField(max_length=250, null=True, blank=True)
    reps1 = models.CharField(max_length=250, null=True, blank=True)
    sets1 = models.CharField(max_length=250, null=True, blank=True)
    exercise2 = models.CharField(max_length=250, null=True, blank=True)
    reps2 = models.CharField(max_length=250, null=True, blank=True)
    sets2 = models.CharField(max_length=250, null=True, blank=True)
    exercise3 = models.CharField(max_length=250, null=True, blank=True)
    reps3 = models.CharField(max_length=250, null=True, blank=True)
    sets3 = models.CharField(max_length=250, null=True, blank=True)
    exercise4 = models.CharField(max_length=250, null=True, blank=True)
    reps4 = models.CharField(max_length=250, null=True, blank=True)
    sets4 = models.CharField(max_length=250, null=True, blank=True)
    exercise5 = models.CharField(max_length=250, null=True, blank=True)
    reps5 = models.CharField(max_length=250, null=True, blank=True)
    sets5 = models.CharField(max_length=250, null=True, blank=True)
    exercise6 = models.CharField(max_length=250, null=True, blank=True)
    reps6 = models.CharField(max_length=250, null=True, blank=True)
    sets6 = models.CharField(max_length=250, null=True, blank=True)
    exercise7 = models.CharField(max_length=250, null=True, blank=True)
    reps7 = models.CharField(max_length=250, null=True, blank=True)
    sets7 = models.CharField(max_length=250, null=True, blank=True)
    exercise8 = models.CharField(max_length=250, null=True, blank=True)
    reps8 = models.CharField(max_length=250, null=True, blank=True)
    sets8 = models.CharField(max_length=250, null=True, blank=True)
    exercise9 = models.CharField(max_length=250, null=True, blank=True)
    reps9 = models.CharField(max_length=250, null=True, blank=True)
    sets9 = models.CharField(max_length=250, null=True, blank=True)
    exercise10 = models.CharField(max_length=250, null=True, blank=True)
    reps10 = models.CharField(max_length=250, null=True, blank=True)
    sets10 = models.CharField(max_length=250, null=True, blank=True)
    gym_or_home = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.user.username
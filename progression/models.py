from django.db import models
from django.contrib.auth.models import User
from Profile.models import Profile

# Create your models here.

class ProgressionPicture(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    week = models.CharField(max_length=250, null=True, blank=True)
    progression_pic = models.ImageField(null=True, blank=True)
    progression_url = models.URLField(null=True, blank=True)
    chest_measurement = models.CharField(max_length=250, null=True, blank=True)
    waist_measurement = models.CharField(max_length=250, null=True, blank=True)
    weight = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.user.username
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ProgressionPicture(models.Model):
    name = models.CharField(max_length=254, null=True, blank=True)
    progression_pic = models.ImageField(null=True, blank=True)
    progression_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.user.username
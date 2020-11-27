from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    progress_pic = models.ImageField(null=True, blank=True)
    chest_measurement = models.DecimalField(max_digits=50, decimal_places=2, null=True, blank=True)
    waist_measurement = models.DecimalField(max_digits=50, decimal_places=2, null=True, blank=True)
    hip_measurement = models.DecimalField(max_digits=50, decimal_places=2, null=True, blank=True)
    exercise = models.CharField(max_length=250, null=True, blank=True)
    sets = models.DecimalField(max_digits=50, decimal_places=0, null=True, blank=True)

    def __str__(self):
        return self.username



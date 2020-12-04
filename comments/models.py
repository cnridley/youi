from django.db import models

# Create your models here.

class comment(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

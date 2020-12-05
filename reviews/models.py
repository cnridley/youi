from django.db import models

# Create your models here.

class Reviews(models.Model):
    My_Rating = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    name = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    rating = models.IntegerField(choices=My_Rating, null=True, blank=True, default=3)
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
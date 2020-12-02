from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.progression_pictures, name='progression_pictures'),
]
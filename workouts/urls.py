from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.workouts_page, name='workouts_page'),
]
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.workouts_page, name='workouts_page'),
    path('edit/<int:workout_id>/', views.edit_workout, name='edit_workout'),
    path('delete/<int:workouts_id>/', views.delete_workout, name='delete_workout'),
]
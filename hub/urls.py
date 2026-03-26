from django.urls import path
from . import views

urlpatterns = [
    path('hub/', views.tracker, name='hub'),
    path('tracker/', views.tracker, name='tracker'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cv/', views.cv, name='cv'),
    path('projects/', views.projects_list, name='projects_list'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
]

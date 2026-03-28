from django.shortcuts import render, get_object_or_404
from .models import Project

def home(request):
    """Home Page"""
    return render(request, 'portfolio/home.html', {})

def cv(request):
    """CV Showcase"""
    return render(request, 'portfolio/cv.html', {})

def projects_list(request):
    """Projects List"""
    projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': projects})

def project_detail(request, pk):
    """Project Showcase"""
    project = get_object_or_404(Project, pk=pk)
    project.tech_list = [t.strip() for t in project.tech_stack.split(',')]
    return render(request, 'portfolio/project_detail.html', {'project': project})

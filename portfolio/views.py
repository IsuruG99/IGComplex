from django.shortcuts import render, get_object_or_404
from .models import Project

def home(request):
    """Main landing page - My name + simple UI"""
    return render(request, 'portfolio/home.html', {})

def cv(request):
    """CV showcase page - PDF link (add your cv.pdf to portfolio/static/portfolio/pdf/cv.pdf)"""
    return render(request, 'portfolio/cv.html', {})

def projects_list(request):
    """Projects overview - cards, one project at a time via detail link"""
    projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': projects})

def project_detail(request, pk):
    """Single project sub-page: Title, Year, Desc, TechStack, Screenshot Viewer"""
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'portfolio/project_detail.html', {'project': project})

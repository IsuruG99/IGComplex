from django.shortcuts import render, get_object_or_404
from .models import Image 

def album(request):
    """Main Outer View"""
    return render(request, 'album/album.html', {})

def gallery(request):
    """Photo Gallery"""
    images = Image.objects.all()
    return render(request, 'album/gallery.html', {'image': images})


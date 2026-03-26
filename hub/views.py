from django.shortcuts import render, get_object_or_404
from .models import Gacha

def hub(request):
    """Hub Main"""
    return render(request, 'hub/hub.html', {})

def tracker(request):
    """Pity Tracker"""
    games = Gacha.objects.all()
    return render(request, 'hub/tracker.html', {'games': games})


from django.shortcuts import render
from .models import Cameras

# Create your views here.
def home(request):
    camera = Cameras.objects.all()
    return render(request, 'camerahub/home.html', {'camera':camera})

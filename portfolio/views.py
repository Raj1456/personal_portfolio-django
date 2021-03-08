from django.shortcuts import render
from .models import Project

def home(requset):
    projects = Project.objects.all()
    return render(requset, 'portfolio/home.html', {'projects':projects})

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'Web_App/index.html')

def sports(request):
    return render(request, 'Web_App/sports.html')
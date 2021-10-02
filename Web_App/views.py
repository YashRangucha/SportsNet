from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def index(request):
    return render(request, 'Web_App/index.html')

def sports(request):
    return render(request, 'Web_App/sports.html')

def organise(request):
    return render(request, 'Web_App/organise.html')

def store(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'Web_App/store.html', context)
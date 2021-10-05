from django.shortcuts import render
from django.http import HttpResponse
from .models import *

import requests
API_KEY = '0e55381042014509ade53f0065695efc'

# Create your views here.

def index(request):
    url = f'https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']


    context = {
        'articles' : articles
    }
    return render(request, 'Web_App/index.html', context)

def sports(request):
    return render(request, 'Web_App/sports.html')

def organise(request):
    return render(request, 'Web_App/organise.html')

def event(request):
    return render(request, 'Web_App/event.html')
    
def store(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'Web_App/store.html', context)

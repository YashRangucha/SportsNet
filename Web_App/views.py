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

def index(request):
    return render(request, 'Web_App/index.html')

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

def organizer(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        sport = request.POST.get('sport')
        email = request.POST.get('email')
        phonenumber = request.POST.get('number')
        address = request.POST.get('address')
        code = request.POST.get('code')
        organizer = Organizer(firstname=firstname, lastname=lastname, sport=sport, email=email,  phonenumber=phonenumber,  address=address,  code=code, ) 
        organizer.save()
      

        return HttpResponse("<h1>Thanks<</h1>")

    return render(request, 'Web_App/organizer.html')

def yashlogin(request):
    return render(request, 'Web_App/yashlogin.html')

def yashregister(request):
    return render(request, 'Web_App/yashregister.html')

def storef(request):
    if request.method == "POST":
        name = request.POST.get('name')
        pname = request.POST.get('pname')
        img = request.POST.get('img')
        local = request.POST.get('local')
        desc = request.POST.get('desc')
        storef = Storef(name=name, pname=pname, img=img, local=local, desc=desc, ) 

        storef.save()

        return HttpResponse("<h1>Thanks<</h1>")
   
    return render(request, 'Web_App/storef.html')

def eventform(request):
     if request.method == "POST":
        name = request.POST.get('name')
        date = request.POST.get('date')
        email = request.POST.get('email')
        number = request.POST.get('number')
        local = request.POST.get('local')
        eventform = Eventform(name=name, date=date, email=email, number=number, local=local, ) 

        eventform.save()

        return HttpResponse("<h1>Thanks<</h1>")

     return render(request, 'Web_App/eventform.html')
   

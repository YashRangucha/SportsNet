from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('sports', views.sports, name="sports"),
    path('organise', views.organise, name="organise"),
    path('event', views.event, name="event"),
    path('store', views.store, name="store"),
    path('storef', views.storef, name="storef"),
    path('eventform', views.eventform, name="eventform"),
    path('organizer', views.organizer, name="organizer"),
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
]

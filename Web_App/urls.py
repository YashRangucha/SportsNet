from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('sports', views.sports, name="sports"),
    path('organise', views.organise, name="organise"),
    path('event', views.event, name="event"),
    path('store', views.store, name="store"),
    path('organizer', views.organizer, name="organizer"),
    path('yashlogin', views.yashlogin, name="yashlogin"),
    path('yashregister', views.yashregister, name="yashregister"),
    path('storef', views.storef, name="storef"),
    path('eventform', views.eventform, name="eventform"),

]

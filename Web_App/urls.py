from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('sports', views.sports, name="sports"),
    path('organise', views.organise, name="organise"),
    path('store', views.store, name="store"),
]

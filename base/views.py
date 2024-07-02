from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Item

# Create your views here.
class Home(ListView):
    model = Item
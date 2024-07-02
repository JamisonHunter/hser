from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Item

# Create your views here.
class Home(ListView):
    model = Item
    template_name = "base/home.html"

class ItemDetail(DetailView):
    model = Item
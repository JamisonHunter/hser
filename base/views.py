from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Item

# Create your views here.
class Home(ListView):
    model = Item
    template_name = "base/home.html"

class ItemDetail(DetailView):
    model = Item

class NewItem(CreateView):
    model = Item
    fields = ["name", "serial", "image"]
    success_url = reverse_lazy("home")
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView    
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from .models import Item

# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy("home")

    

class Home(ListView):
    model = Item
    template_name = "base/home.html"

class ItemDetail(DetailView):
    model = Item

class NewItem(CreateView):
    model = Item
    fields = ["user", "name", "serial", "image"]
    success_url = reverse_lazy("home")

class UpdateItem(UpdateView):
    model = Item
    fields = ["user", "name", "serial", "image"]
    success_url = reverse_lazy("home")

class DeleteItem(DeleteView):
    model = Item
    success_url = reverse_lazy("home")

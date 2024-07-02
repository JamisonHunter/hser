from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Item

# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("home")

class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(RegisterPage, self).get(*args, **kwargs)

class Home(LoginRequiredMixin, ListView):
    model = Item
    template_name = "base/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = context['object_list'].filter(user=self.request.user)

        search_input = self.request.GET.get("search-area") or ""
        if search_input: 
            context['object_list'] = context['object_list'].filter(name__icontains=search_input)
        context["search_input"] = search_input
        return context

class ItemDetail(LoginRequiredMixin, DetailView):
    model = Item

class NewItem(LoginRequiredMixin, CreateView):
    model = Item
    fields = ["name", "serial", "image"]
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(NewItem, self).form_valid(form)

class UpdateItem(LoginRequiredMixin, UpdateView):
    model = Item
    fields = ["name", "serial", "image"]
    success_url = reverse_lazy("home")

class DeleteItem(LoginRequiredMixin, DeleteView):
    model = Item
    success_url = reverse_lazy("home")
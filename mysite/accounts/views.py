from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView, CreateView
from .forms import SignUpForm
from django.urls import reverse_lazy
# Create your views here.


class signinView(CreateView):
    form_class = SignUpForm
    template_name = "auth/register.html"
    success_url = reverse_lazy("home:welcome")

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return response
    

class loginView(TemplateView):
    template_name = "auth/login.html"
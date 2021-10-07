from django.shortcuts import get_list_or_404, render, redirect, get_object_or_404
from django.urls.base import reverse_lazy, reverse
from django.contrib import messages
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import get_user_model, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetView, PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.http import require_POST
from account.models import CustomUser
from account.forms import CustomRegisterForm

# Create your views here.

class CustomRegisterView(CreateView):
    model = CustomUser
    template_name = "account/connexion.html"
    success_url = reverse_lazy('account:login')
    title = "default"
    form_class = CustomRegisterForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = "Création d'un compte"
        context['submit'] = "Créer"
        return context

class CustomLoginView(LoginView):
    model = CustomUser
    form_class = AuthenticationForm
    title = "default"
    success_url = reverse_lazy('memorize:home')
    template_name = "account/connexion.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Se connecter"
        context['submit'] = "Connection"
        session = self.request.session
        session['win'] = 0
        session['tryied'] = 0
        return context


class CustomLogOutView(LogoutView):
    next_page = '/'

class Profil(TemplateView):
    template_name = 'account/profil.html'
    
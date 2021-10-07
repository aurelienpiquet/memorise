from django.contrib import admin
from django.urls import path, include

from account.views import *

app_name = 'account'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name="login"),
    path('register/', CustomRegisterView.as_view(), name="register"),
    path('log-out/', CustomLogOutView.as_view(), name="logout"),
    path('profil', Profil.as_view(), name="profil")
]
    
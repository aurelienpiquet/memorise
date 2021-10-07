
from django import forms
from django.forms import MultiWidget
from django.forms.widgets import CheckboxSelectMultiple, NumberInput, SelectDateWidget, DateInput, DateTimeInput
from django.contrib.auth.forms import UserCreationForm
from account.models import CustomUser


import datetime
from django.core.validators import MinValueValidator, MaxValueValidator

class CustomRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email',)




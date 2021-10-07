
from django import forms
from django.forms import MultiWidget
from django.forms.widgets import CheckboxSelectMultiple, NumberInput, SelectDateWidget, DateInput, DateTimeInput
from django.contrib.auth.forms import UserCreationForm
from memorize.models import Task, Category


import datetime
from django.core.validators import MinValueValidator, MaxValueValidator

categories = Category.objects.all()
CATEGORY = [(categorie.title, categorie.title) for categorie in categories]

class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('category', 'title')
        widgets = {'category' : forms.RadioSelect(), 
                    'title' : forms.TextInput(attrs={'placeholder' : "Ecrivez le nom de votre tâche ici et Entrée..."})}

    







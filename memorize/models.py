from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.core.validators import RegexValidator
from account.models import CustomUser
from datetime import datetime
# Create your models here.

phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")   
User = get_user_model()

class Category(models.Model):
    title = models.CharField(max_length=255, blank=False, verbose_name="titre")
    color = models.CharField(max_length=255, blank=True, verbose_name="couleur")
    thumbnail = models.ImageField(max_length=255, blank=True, upload_to="categories")

    class Meta:
        verbose_name = "Catégorie"

    def __str__(self):
        return self.title

class Status(models.Model):
    title = models.CharField(max_length=255, blank=False, verbose_name="titre")
    slug = models.SlugField(max_length=255, blank=True, verbose_name="slug")

    class Meta:
        verbose_name = "Statu"
    
    def save(self, *args, **kwargs):
        if not self.slug :
           self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Task(models.Model):
    title = models.CharField(max_length=500, blank=False, verbose_name="Nouvelle tâche")
    subtitle = models.CharField(max_length=255, blank=True, verbose_name="Sous-titre")
    created_on = models.DateTimeField(auto_now_add=True)
    made_on = models.CharField(default="none", blank=True, max_length=255, verbose_name="date de réalisation")
    remind = models.BooleanField(default=False, blank=False)
    category = models.ForeignKey(Category, verbose_name="Catégories", on_delete=models.SET_NULL, null=True)
    status = models.ForeignKey(Status, verbose_name="status", on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, verbose_name="Utilisateur", on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Tache"

    def save(self, *args, **kwargs):
        self.title = self.title.capitalize()
        if not self.subtitle :
           self.subtitle = slugify(self.title)
        if not self.status : 
            self.status = Status.objects.get(pk=1)
        super().save(*args, **kwargs)
    
    def modify_status(self):
        if self.status.pk < 3 :
            self.status = Status.objects.get(pk = self.status.pk + 1)
            self.made_on = datetime.now().strftime("%d-%m-%y")
        self.save()

    def created_on_str(self):
        return self.created_on.date()

    def __str__(self):
        return self.title

class Contact(models.Model):
    firstname = models.CharField(max_length=255, blank=False)
    lastname = models.CharField(max_length=255, blank=False)
    email = models.EmailField(max_length=255, blank=False)
    phone = models.CharField(max_length=255, blank=False)

class FoodGame(models.Model):
    question = models.CharField(max_length=255, blank=False, verbose_name="Question")
    option = models.CharField(max_length=255, blank=False,default="none", verbose_name="Différentes options")
    answer = models.CharField(max_length=255, blank=False, verbose_name="Réponse")

    class Meta:
        verbose_name = 'Questionnaire sur les Menu'

    def __str__(self):
        return self.question[:50]

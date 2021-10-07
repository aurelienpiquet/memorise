
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator


# Create your models here.

phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")    

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Vous devez entrer un email.')
        user = self.model(
            email = self.normalize_email(email)
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email=email, password=password)
        user.is_admin = True
        user.is_staff = True
        user.save() 
        return user

class CustomUser(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True, blank=False)
    firstname = models.CharField(max_length=255, null=True, blank=True)
    lastname = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    phoneNumber = models.CharField(validators = [phoneNumberRegex], max_length = 16, blank=True, verbose_name="Téléphone")
    ip = models.CharField(max_length=255, null=True, blank=True)
    last_login = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'email'
    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Utilisateur'

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True

    def last_login_str(self):
        return self.last_login.date()
from django.contrib import admin
from account.models import *
# Register your models here.

@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    empty_value_display = "-"

    list_display = ('email', 'is_admin')


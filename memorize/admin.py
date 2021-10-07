from django.contrib import admin
from memorize.models import *

# Register your models here.


@admin.register(Task)
class UserAdmin(admin.ModelAdmin):
    empty_value_display = "-"

    list_display = ('pk', 'title', 'created_on', 'status')

@admin.register(Category)
class UserAdmin(admin.ModelAdmin):
    empty_value_display = "-"

    list_display = ('title','color')

@admin.register(Status)
class UserAdmin(admin.ModelAdmin):
    empty_value_display = "-"
    list_display = ('pk', 'title', 'slug')

@admin.register(FoodGame)
class UserAdmin(admin.ModelAdmin):
    empty_value_display = "-"

    list_display = ('question', 'option', 'answer')


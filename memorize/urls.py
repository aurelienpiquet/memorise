from django.contrib import admin
from django.urls import path, include

from memorize.views import *

app_name = 'memorize'

urlpatterns = [
    path('', CustomHomeView.as_view(), name="home"),
    path('checked/<int:pk>', taskChecked, name="checked"),
    path('create', addTask, name="create"),
    path('game-reminder/', reminderGameTask, name="reminder-game"),
    path('game-reminder-check/<pk>/', reminderGameTaskCheck, name="reminder-game-check"),
    path('game-food/', foodGameTask, name="food-game"),
    path('game-food-check/<int:pk>/<str:option>/', foodGameTaskCheck, name="food-game-check"),
    path('game-reset-reminder/', resetScoreReminder, name="reset-game-score-reminder"),
    path('game-reset-food/', resetScoreFood, name="reset-game-score-food"),
]

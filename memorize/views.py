from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_list_or_404, render, redirect, get_object_or_404
from django.urls.base import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
from memorize.models import Task, Category, FoodGame
from memorize.forms import AddTaskForm
import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class CustomHomeView(TemplateView):
    template_name = 'memorize/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Bienvenu"
        if self.request.user.is_authenticated:
            context['tasks'] = Task.objects.filter(user = self.request.user).all()
        context['form'] = AddTaskForm()
        try :
            context['username'] = self.request.user.email.split('@')[0]
        except IndexError:
            context['username'] = self.request.user
        return context

@login_required
def taskChecked(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.modify_status()
    return redirect('memorize:home')

@login_required
def addTask(request):
    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        form.instance.user = request.user
        form.save()
    return redirect('memorize:home')

@login_required
def reminderGameTask(request):
    test_ok = False
    count = 0
    while not test_ok:
        tasks = Task.objects.filter(user=request.user).exclude(status__pk = 3).order_by('?')[:3]
        count += 1
        for task in tasks:
            if task.made_on == datetime.datetime.now().strftime("%d-%m-%y"):
                test_ok = True
        if count == 3 :
            test_ok = True
                
    question = "Quelle activité avez-vous réalisés en aujourd'hui?"
    session = request.session
    win = session['win']
    tryied = session['tryied']
    title = "Reminder Game"
    return render(request, 'memorize/remind-game.html', context = {"tasks" : tasks, "question" : question, 'win':win, 
        'tryied' : tryied, 'title' : title})

@login_required
def reminderGameTaskCheck(request, pk):
    if request.method == 'GET':
        session = request.session
        task = get_object_or_404(Task, pk=pk)
        if task.made_on == datetime.datetime.now().strftime("%d-%m-%y") and task.status.pk > 1 :
            messages.success(request, "Bravo, C'est la bonne réponse.")
            session['win'] = 1 if session['win'] < 1 else session['win'] + 1
        else:
            messages.error(request, "Perdu, Ce n'était pas la bonne réponse.")
        session['tryied'] = 1 if session['tryied'] < 1 else session['tryied'] + 1
    return redirect('memorize:reminder-game')

@login_required
def foodGameTask(request):
    title = "Reminder Game"
    session = request.session
    win = session['win']
    tryied = session['tryied']
    question = FoodGame.objects.order_by('?')[0]
    options = question.option.split('.')
    return render(request, 'memorize/food-game.html', context = {'title' : title, 'win' : win, 'tryied' : tryied, 'question' : question, "options" : options})

@login_required
def foodGameTaskCheck(request, option, pk):
    if request.method == 'GET': 
        session = request.session
        answer = FoodGame.objects.get(pk=pk).answer
        if answer == option : 
            messages.success(request, "Bravo, C'est la bonne réponse.")
            session['win'] = 1 if session['win'] < 1 else session['win'] + 1
        else:
            messages.error(request, "Perdu, Ce n'était pas la bonne réponse.")
        session['tryied'] = 1 if session['tryied'] < 1 else session['tryied'] + 1
        return redirect('memorize:food-game')

@login_required
def resetScoreFood(request):
    if request.method == 'POST':
        request.session['win'] = 0
        request.session['tryied'] = 0
    return redirect('memorize:food-game')

@login_required
def resetScoreReminder(request):
    if request.method == 'POST':
        request.session['win'] = 0
        request.session['tryied'] = 0
    return redirect('memorize:reminder-game')


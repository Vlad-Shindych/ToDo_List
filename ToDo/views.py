from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .forms import TaskForm, CategoryForm


def start(request):
    return HttpResponse('Главная страница')


def all_users(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render (request, "listusers.html", context)


def pers_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    context = {
        'user': user,
    }
    return render(request, "pers_user.html", context)

def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'create_task.html', context)

def create_category(request):
    if request.method == "POST":
        form = CategoryForm(reqпuest.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CategoryForm()
        context = {

        'form': form
    }
    return render(request, "create_task.html", context)
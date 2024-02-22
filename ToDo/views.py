from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


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

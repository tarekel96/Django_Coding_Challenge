from django.shortcuts import render
from django.http import HttpResponse
from .userController import *

# Create your views here.


def home(request, id=1):
    user = user_by_id(id)
    id = user.id
    context = {'user': user, "id": id}
    return render(request, 'challenge/home.html', context)


def profile(request, id=1):
    user = user_by_id(id)
    id = user.id
    context = {'user': user, "id": id}
    return render(request, 'challenge/profile.html', context)

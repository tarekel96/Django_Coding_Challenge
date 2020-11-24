from django.shortcuts import render
from django.http import HttpResponse
from .userController import *

# Create your views here.


def home(request):
    return render(request, 'challenge/home.html')


def profile(request):
    user = first_user()
    return render(request, 'challenge/profile.html', {'user': user})

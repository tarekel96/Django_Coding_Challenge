from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'challenge/home.html')


def profile(request):
    return render(request, 'challenge/profile.html')

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(response):
    return HttpResponse("Home")


def profile(response):
    return HttpResponse("Profile")

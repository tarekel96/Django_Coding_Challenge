from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(response):
    return HttpResponse("home")


def profile(response):
    return HttpResponse("profile")

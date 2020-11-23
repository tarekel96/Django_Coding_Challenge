from django.urls import path
from .views import home
from .views import profile

urlpatterns = [
    path('', home),
    path("profile/", profile)
]

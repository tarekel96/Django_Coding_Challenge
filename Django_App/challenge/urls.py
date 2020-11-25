from django.urls import path
from .views import home
from .views import profile
from . import views

urlpatterns = [
    path('', home),
    path('<int:id>', home),
    path('profile/', profile, name="profile"),
    path('profile/<int:id>/', profile, name="profile")
]

from django.urls import path
from .views import home
from .views import profile
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', home),
    path('<int:id>', home),
    path('profile/', profile, name="profile"),
    path('profile/<int:id>/', profile, name="profile")
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

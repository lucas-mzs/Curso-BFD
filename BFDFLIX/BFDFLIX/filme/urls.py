# Ao criar uma página, precisamos configurar a URL, o VIEW e o TEMPLATE.

from django.urls import path
from django.urls import include
from .views import homepage

urlpatterns = [
    path('', homepage)
]
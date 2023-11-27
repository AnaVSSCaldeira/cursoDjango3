from django.urls import path, include
from .views import hello_test

urlpatterns = [
    path('', hello_test),
]
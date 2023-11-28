from django.urls import path, include
from .views import hello_test, post_detail

urlpatterns = [
    path('', hello_test, name = 'index_website'),
    path('post/<int:id>/', post_detail, name = 'post_detail_name'),
]
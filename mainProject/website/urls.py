from django.urls import path, include
from .views import hello_test, post_detail, save_form

urlpatterns = [
    path('', hello_test, name = 'index_website'),
    path('post/<int:id>/', post_detail, name = 'post_detail_name'),
    path('save-form/', save_form, name = 'save_form')
]
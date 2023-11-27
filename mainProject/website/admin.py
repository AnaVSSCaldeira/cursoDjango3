from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from .models import Post



class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'catogories', 'approved']

    def get_queryset(self, request):
        return Post.objects.all() # pode filtrar se quiser

admin.site.register(Post, PostAdmin)
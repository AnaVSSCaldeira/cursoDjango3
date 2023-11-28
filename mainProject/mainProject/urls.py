from django.contrib import admin
from django.urls import path, include
from .views import hello_world
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_world),
    path('website/', include('website.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
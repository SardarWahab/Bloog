from django.contrib import admin
from django.urls import path
from Blog.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home)
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
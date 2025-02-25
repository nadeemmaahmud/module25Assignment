from django.contrib import admin
from django.urls import path, include

from contents.views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('contents.urls')),
]

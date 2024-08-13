from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.http import HttpResponse
import os

def home(request):
    name = os.getenv('NAME')
    user = os.getenv('USER')
    host = os.getenv('HOST')
    return HttpResponse(f'Hello World{name} {host} {user}')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home')
]

urlpatterns += staticfiles_urlpatterns()
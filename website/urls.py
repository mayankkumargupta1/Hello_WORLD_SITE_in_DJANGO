from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.http import HttpResponse
import os

def home(request):
    name = os.getenv('DATABASE_URL')
    return HttpResponse(f'Hello World{name}')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home')
]

urlpatterns += staticfiles_urlpatterns()
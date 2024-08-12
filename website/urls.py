from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello World')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home')
]

urlpatterns += staticfiles_urlpatterns()
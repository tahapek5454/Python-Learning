from django.urls import path
from . import views

# http://127.0.0.1:8000/
# benim localhostumdaki 8000 portunda yayımalnacak

urlpatterns = [
    path('', views.index, name='index'), # ilk parametrenin bos olmasi ana hostta kalamamız
    path('about', views.about, name='about') # http://127.0.0.1:8000/about
]
"""blogapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# diger app lerden gelen urls leri aktarmak icin include u import ettin


# http://127.0.0.1:8000/ ==> index.html
# http://127.0.0.1:8000/index ==> index.html
# http://127.0.0.1:8000/blog ==> blog.html
# http://127.0.0.1:8000/blog/3 ==> blog-details

# include ederken tirak icini bos biraktım eger doldursam mesele user yazsam
# http://127.0.0.1:8000/user/ bu sekilde baslardi hepsi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]

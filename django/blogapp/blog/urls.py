
from django.urls import path
from . import views
# uygulamamızın ana adresi bu sekilde

# http://127.0.0.1:8000/ ==> index.html
# http://127.0.0.1:8000/index ==> index.html
# http://127.0.0.1:8000/blog ==> blog.html
# http://127.0.0.1:8000/blog/3 ==> blog-details

# burda serverla arasındaki iletişim url lerini belirliyoruz
# bize ne dondursun !

# Yukarırdaki tanımlamalarda views içersindeki bilgili url e aktarmak için
# onu import etmemiz gerekti.

# bu urls leri ana uygulamaya tanımayı unutma

urlpatterns = [
    path("",views.index, name='home'), # burada tirnakları bos birakınca eklentisiz anlamına geliyor, name ise bu linki kullanmak için lazım
    path("index",views.index), # artik index yazdıktan sonra da gelsin dedik
    path("blogs",views.blogs, name='blogs'),
    path("blogs/<int:id>",views.blogs_details, name='blogs_details'), # <int:id> int tipinde id adında bir degisken gelicek
]

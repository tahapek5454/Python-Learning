from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.

# burası da bizim sayfalarda neler gozuksun onların komutlarının verildiği yer
# url belirtirken ilgili url de hangi bilgilerin gozukecegi burdan belirleniyor

# request parametresinin gelmesi bu sayfaların açılması için bir isteğe ihtiyaç duyması

def index(request):
    return HttpResponse("Home Page")

def blogs(request):
    return HttpResponse('Blogs Page')

def blogs_details(request, id):
    # block details ın id alma sebebi url kısmında değişken bir <int:id> deger gelecegini 
    # belirtmemiz gelen degeree gore islem yapacagiz
    return HttpResponse('Blogs-details id : '+ str(id))

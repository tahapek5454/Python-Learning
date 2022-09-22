from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.

# burası da bizim sayfalarda neler gozuksun onların komutlarının verildiği yer
# url belirtirken ilgili url de hangi bilgilerin gozukecegi burdan belirleniyor

# request parametresinin gelmesi bu sayfaların açılması için bir isteğe ihtiyaç duyması

# render bize html dosyalarını göndermemizi sağlıyor
# render a request ve ilgili templates klosorundeki html sayfalarını gönderiyor
# tüm uygulamalardaki templates kolosorlerine baktığından karışmaması adına biz klosor klosor yapalım

def index(request):
    return render(request, "blog/index.html")

def blogs(request):
    return render(request, 'blog/blogs.html')

def blogs_details(request, id):
    # block details ın id alma sebebi url kısmında değişken bir <int:id> deger gelecegini 
    # belirtmemiz gelen degeree gore islem yapacagiz

    # bizim parametre olarak gelen id yi kullanammız icin 3. parametreye key value seklinde
    # gelen id yi gondermemiz lazım
    return render(request, "blog/blogs_details.html", {
        "id": id,
    })

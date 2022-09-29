from multiprocessing import context
from select import select
from unicodedata import category
from django.http.response import HttpResponse
from django.shortcuts import render
from blog.models import Blog, Category
# bu importu db den blog ları ve caegoryleri dinamik cekmek icin aldık


# Create your views here.

# burası da bizim sayfalarda neler gozuksun onların komutlarının verildiği yer
# url belirtirken ilgili url de hangi bilgilerin gozukecegi burdan belirleniyor

# request parametresinin gelmesi bu sayfaların açılması için bir isteğe ihtiyaç duyması

# render bize html dosyalarını göndermemizi sağlıyor
# render a request ve ilgili templates klosorundeki html sayfalarını gönderiyor
# tüm uygulamalardaki templates kolosorlerine baktığından karışmaması adına biz klosor klosor yapalım


# dinamik veri isleme temellerini atıyoruz
data = {
    'blogs':[
        {
        'id':1,
        'title':'web gelistirme',
        'image':'1.png',
        'is_active':True,
        'is_home':False,
        'description':'cok iyi bit kurs'
        },
        {
        'id':2,
        'title':'react gelistirme',
        'image':'2.png',
        'is_active':True,
        'is_home':True,
        'description':'cok iyi bit kurs'
        },
        {
        'id':3,
        'title':'c# gelistirme',
        'image':'3.png',
        'is_active':False,
        'is_home':True,
        'description':'cok iyi bit kurs'
        }
    ]
}
# fakat artık db den veri cekcegimizden bunu kullanmauacagiz
def index(request):

    # data yı sayfaya yollamamız icin
    # context = {
    #     'blogs':data['blogs']
    # }
    # bunu artık dinamik db den cekmek icin kullanmayacagiz

    context = {
        'blogs':Blog.objects.filter(is_home=True, is_active = True),
        'categories':Category.objects.all()
        # filtreleme islemi
        # bu sekilde all diyerek tum verileri alrızı
    }



    # iceri de aktarmak icin parametre olarak yolladık
    return render(request, "blog/index.html", context)

def blogs(request):

    # data yı sayfaya yollamamız icin key value lazım onun da key i ile islem yapıyorsun
     # data yı sayfaya yollamamız icin
    # context = {
    #     'blogs':data['blogs']
    # }
    # bunu artık dinamik db den cekmek icin kullanmayacagiz

    context = {
        'blogs':Blog.objects.filter(is_active = True),
        'categories':Category.objects.all()
        # bu sekilde all diyerek tum verileri alrızı
    }


    # iceri de aktarmak icin parametre olarak yolladık
    return render(request, 'blog/blogs.html',context)

def blogs_details(request, slug):
    # id ler slug a dondu
    # block details ın id alma sebebi url kısmında değişken bir <int:id> deger gelecegini 
    # belirtmemiz gelen degeree gore islem yapacagiz

    # bizim parametre olarak gelen id yi kullanammız icin 3. parametreye key value seklinde
    # gelen id yi gondermemiz lazım

    # blogs = data['blogs']
    # selected_blog = None

    # for blog in blogs:
    #     if blog['id'] == id:
    #         selected_blog = blog
    # burdaki islemler sayesşnde secili blogu aldık ve onu sayfay gonderdik
    # artik bu islemlere gerek yok basitce filtreleyelim

    
    selected_blog = Blog.objects.get(slug=slug)
    # get bize bir sonuc dondurur digerleri liste
    print(selected_blog)

    return render(request, "blog/blogs_details.html", {
        "blog": selected_blog,
        'category':Category.objects.all()
    })


def blogs_by_category(request, slug):
    # burda filtrelee islemini gerceklestirecegiz
    # filtreleme isleminde bize category lazımdı
    # bu category foreign keydi biz key e ulastıktan sonra keydeki slug bilgisine ulasmlaıyız
    # onun syntax o da category__slug gibi 
    context = {
        'blogs':Blog.objects.filter(is_active = True, category__slug = slug),
        'categories':Category.objects.all(),
        'selectedCategory':Category.objects.get(slug = slug)
        # bu sekilde all diyerek tum verileri alrızı
    }


    # iceri de aktarmak icin parametre olarak yolladık
    return render(request, 'blog/blogs.html',context)


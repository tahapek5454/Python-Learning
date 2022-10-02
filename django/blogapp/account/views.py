from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
# authenticate method bize gelen username passwordun giris yapıp yapacagını bulmaya yarıyor
# login iste bizim tarayıcı üzerinde sessiona drekt cookie yi ekliyor hesanı loginletiyor

# Create your views here.


def login_request(request):

    # biz eger post islemi yapıldsıysa if blogu icersindekileri
    # gerceklestirecegiz bunu kontorlu request icersindeki methoddan bakacagız
    # akti takdirde bu ssayfaya istek geldiyse sayfa arayuzunu gosterecegiz

    if request.method == "POST":
        userName = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username = userName, password = password)
        # eger boyle bir kullanıcı varsa giris payabilir bize o kullanucu dondurur

        if user is not None:
            login(request, user)
            # login i istegi ve kullanıcıyı veridk
            return redirect("home") # kayıt olunda home dan deva
        else:
            return render(request, "account/login.html", {
                "eror": "Kullanici adi veya sifre yanlis"
            })
            # boyle bir kullanıcı yoksa tekrar loin sayfasını verelim
            # ve bir error atalım

    return render(request, "account/login.html")


def register_request(request):

    return render(request, "account/register.html")


def logout_request(request):

    return redirect('home') # direkt gonderir

from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
# authenticate method bize gelen username passwordun giris yapıp yapacagını bulmaya yarıyor
# login iste bizim tarayıcı üzerinde sessiona drekt cookie yi ekliyor hesanı loginletiyor
# logout ise direkt sessiondan silip log out ettiriyor
from django.contrib.auth.models import User
# bu class bizim userlar uzerinden islem yapmaıza ve user eklememizi saglayacak

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

    if request.method == "POST":
        email = request.POST["email"]
        firstName = request.POST["firstname"]
        lastName = request.POST["lastname"]
        userName = request.POST["username"]
        password = request.POST["password"]
        rePassword = request.POST["repassword"]
    
        if password == rePassword:
            if User.objects.filter(username = userName).exists():
                # bu metodu biz bu isimle kayutlu bir kullanıcı dah once var mı diye kontrol ediyoruz
                return render(request, "account/register.html", {
                "eror" : "Kullanici adi daha onceden olusturulmustur."
                })
            elif User.objects.filter(email = email).exists():
                return render(request, "account/register.html", {
                "eror" : "Email daha onceden olusturulmustur."
                })
            else:
                # her sey yolundadir bir user olusturalım
                user  = User.objects.create_user(username=userName, email=email, first_name = firstName,
                                                last_name =lastName, password=password )
                # burda User objesinin tanımına gidip parametreli ogrenebiilirs inheritance
                # create_user sifreleri falan hashleyerek yolluyor
                user.save() # ile de kayıt ettik

                return redirect('login')



        else:
            return render(request, "account/register.html", {
                "eror" : "Sifreler uyusmuyor. Lutfen kontrol ediniz"
            })

    return render(request, "account/register.html")


def logout_request(request):

    logout(request) # request icersindeki userin session id sini siler log out eder

    return redirect('home') # direkt gonderir

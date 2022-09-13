from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages



# Create your views here.

def login(request):
    if request.method == 'POST':
        # get datas
        userName = request.POST['username']
        
        password = request.POST['password']
        
        user = auth.authenticate(username= userName, password= password)
        if user is not None:
            auth.login(request, user)
            messages.add_message(request, messages.SUCCESS, 'Login Basarili')
            return redirect('index')
        else:
            messages.add_message(request, messages.ERROR, 'Kullanici Adi Veya Sifre Hatali')
            return redirect('login')
                

    return render(request, 'user/login.html')

    
        

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.add_message(request, messages.SUCCESS, 'Oturum Kapatıldı')
        return redirect('index')

    return render(request, 'user/logout.html')

def register(request):
    if request.method == 'POST':
        # get datas
        userName = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if repassword == password:
            if User.objects.filter(username = userName).exists():
                 messages.add_message(request, messages.WARNING, 'Kullanıcı adı daha once alinmis')
            elif User.objects.filter(email = email).exists():
                 messages.add_message(request, messages.WARNING, 'Email daha once alinmis')
            else:
                # her sey yolunda
                user = User.objects.create_user(username= userName, email= email, password= password)
                user.save()
                messages.add_message(request, messages.SUCCESS, 'Kullanici Olusturuldu')
                return redirect('login')
        else:
            messages.add_message(request, messages.WARNING, 'Sifreler eslesmiyor')
            return redirect('register')
                

    return render(request, 'user/register.html')
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

import user

# Create your views here.

def login(request):
    if request.method == 'POST':
        # get datas
        userName = request.POST['username']
        
        password = request.POST['password']
        
        user = auth.authenticate(username= userName, password= password)
        if user is not None:
            auth.login(request, user)
            print('login basarlili')
            return redirect('index')
        else:
            print('Kullanici adi veya sifre hatali')
            return redirect('login')
                

    return render(request, 'user/login.html')

    
        

def logout(request):
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
                print('Kullanıcı adı daha once alinmis')
            elif User.objects.filter(email = email).exists():
                print('Email daha once alinmis')
            else:
                # her sey yolunda
                user = User.objects.create_user(username= userName, email= email, password= password)
                user.save()
                print('Kullanici Olusturuldu')
                return redirect('login')
        else:
            print('Sifreler eslesmiyor')
            return redirect('register')
                

    return render(request, 'user/register.html')


import json
import os


class User:

    def __init__(self,username,password,email) -> None:
        self.username = username
        self.password = password
        self.email = email

class UserRepository:
    

    def __init__(self) -> None:
        
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}

        # load users from .json file

        self.loadUsers()

    def loadUsers(self):
        
        if os.path.exists("users.json"):

            with open("users.json","r") as file:

                users = json.load(file) # dosyadan json modunda okuma

                for user in users:
                    user = json.loads(user) # json dan python objesine
                    #print(user["username"])
                    newUser = User(user["username"],user["password"],user["email"])
                    self.users.append(newUser)          
        else:
            print("Goremedim")


    def register(self , user : User): # veri kaydetme

        self.users.append(user)

        # save to file

        self.saveToFile()

        print("Kayit yapildi")
        

    def login(self,username,password):   # veri giris
        
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentUser = user
                print("Giris yapildi")
                break


    def logOut(self):
        self.isLoggedIn = False
        self.currentUser = {}
        print("Cikis yapildi")

    def identity(self):

        if self.isLoggedIn:
            print("Username : {} Passsword : {} Email : {}".format(self.currentUser.username,self.currentUser.password,self.currentUser.email))  

    def saveToFile(self):  # json modelde kayit edicek verileri

        list =[]

        for user in self.users:

            list.append(json.dumps(user.__dict__)) # bu islemde class dict e cevriliyor dict de json modele
        
        with open("users.json","w") as file:

            json.dump(list,file) # Direkt class kaydedemiyoruz dict e cevirecegiz


# Program calistigi surece olmasi icin dongu disina tanımla yaptil

repo = UserRepository()

while True:
    # Menumuz

    print("Menu".center(50,"-"))

    secim = input("1-) Register\n2-) Login\n3-) LogOut\n4-) Identity\n5-) Exit\nSeciminizi Yapiniz : ")

    if secim == '5':
        print("Cikis yapildi")
        break

    elif secim == '1':
        #register
        
        userName = input("Kullanici adi giriniz : ")
        password = input("Sifre giriniz : ")
        email = input("Emailinizi giriniz : ")

        user = User(userName,password,email)

        repo.register(user)

        

    elif secim == '2':
        #login
        username = input("Kullanici adinizi giriniz : ")
        password = input("Sifrenizi giriniz : ")
        
        repo.login(username,password)

    elif secim == '3':
        #logout
        repo.logOut()
    elif secim == '4':
        #identity
        repo.identity()
    else:
        print("Yanlis Secim Tekrar Deneyiniz")



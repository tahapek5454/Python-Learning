

# amac kod uzerinden github ile ilgili islemleri yapmak





import requests 


class Github:
    
    def __init__(self) -> None:
        self.api_url = "https://api.github.com"
    
    def getUser(self,userName):

        response = requests.get(self.api_url+"/users/"+userName)
        # donus tipi olarak json modeli dict e cevirelim kisa yontemle
        return response.json()

    def getRepositories(self,userName):
        response = requests.get(self.api_url+"/users/"+userName+"/repos")
        return response.json()

github = Github()

while True:

    menu = "1-)Find User\n2-)Get Repository\n4-)Exit"
    print(menu)
    secim = input("Seciminizi yapiniz : ")

    if secim=="4":
        print("Uygulama sonlanmistir...")
        break
    elif secim=="1":
        # find user 
          
        userName = input("Kullanici adini giriniz : ")
        result = github.getUser(userName)
        print(f"name : {result['name']} \n public repos : {result['public_repos']} \n followers : {result['followers']}")

    elif secim=="2":
        # find repo
        
        userName = input("Kullanici adini giriniz : ")
        result = github.getRepositories(userName)
        # burdan bize bir liste halinde json model gelicek

        for i in result:
            print(f"name : {i['name']}")

    else:
        print("Yanlis secim yapilmistir lutfen tekrar deneyiniz")

    
from selenium import webdriver
import time
import kimlik as k

class Browser:
    def __init__(self,link) -> None:
        try:
            self.link = link
            self.takipciler = []
            self.takip_edilenler = []
            self.browser = webdriver.Chrome(r"C:\Users\90543\Desktop\VS\python\web-driver\chromedriver.exe")
            Browser.goInstagram(self)
            Browser.getExceptFollowers(self,Browser.diff(self,self.takip_edilenler,self.takipciler))
        except Exception as  ex :
            print("Bir hata")
            print("-"*100)
            print(ex)


    def goInstagram(self):
        self.browser.get(self.link)
        time.sleep(2)
        Browser.login(self)   
        Browser.getFollowers(self)
        time.sleep(2)
        self.browser.get(self.link+"/"+k.username)
        time.sleep(2)
        Browser.getFollowUp(self)
 
    def getFollowers(self):
        time.sleep(2)
        self.browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[2]/a").click()
        time.sleep(2)

        Browser.scroollDown(self)
        sayac = 0
        takipciler = self.browser.find_elements_by_css_selector("._aacl._aaco._aacw._aacx._aad7._aade")
        print("*"*100)
        for i in takipciler:
            sayac+=1
            self.takipciler.append(i.text)
            #print(str(sayac)+"-)"+i.text)
    
    def getFollowUp(self):
        time.sleep(2)
        self.browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[3]/a").click()
        time.sleep(2)

        Browser.scroollDown(self)

        takip = self.browser.find_elements_by_css_selector("._aacl._aaco._aacw._aacx._aad7._aade")
        print("*"*100)
        sayac = 0
        for i in takip:
            sayac+=1
            self.takip_edilenler.append(i.text)
            #print(str(sayac)+"-)"+i.text)
                
    def scroollDown(self):
        jsKomutu = """
        sayfa = document.querySelector("._aano");
        sayfa.scrollTo(0,sayfa.scrollHeight);
        var sayfaSonu = sayfa.scrollHeight;
        return sayfaSonu; 
        """

        sayfa_sonu = self.browser.execute_script(jsKomutu)

        while True:
            son = sayfa_sonu
            time.sleep(3)
            sayfa_sonu = self.browser.execute_script(jsKomutu)
            if son == sayfa_sonu:
                break
		
    def getExceptFollowers(self,listem):
        time.sleep(1)
        
        print("Senin takip ettigin ama seni takip etmeyen hesaplar...")
        sayac = 0
        print("Takipci sayin = "+str(len(self.takipciler)))
        print("Takip sayin = "+str(len(self.takip_edilenler)))
        print("*"*100)
        for i in listem:
            sayac+=1
            print(str(sayac)+"-)"+i)
        print("*"*100)
    
    def diff(self,list1, list2):
        time.sleep(2)
        c = set(list1)-set(list2) 
        return list(c)
        
    def login(self):
        username = self.browser.find_element_by_name('username')
        password = self.browser.find_element_by_name('password')

        username.send_keys(k.username)
        password.send_keys(k.password)
        time.sleep(1)

        btn = self.browser.find_element_by_css_selector('#loginForm > div > div:nth-child(3)')
        btn.click()
        time.sleep(5)
        
        self.browser.get(self.link+"/"+k.username)
        time.sleep(1)

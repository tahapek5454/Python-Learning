
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# your account

userName = "YourUserName"
password = "YourPassword"

# your account

class Instagram:
    def __init__(self,username,password) -> None:
        self.driver = webdriver.Chrome(r'C:\Users\90543\Desktop\VS\python\web-driver\chromedriver.exe')
        self.userName = username
        self.password = password
    
    def logIn(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(1)
        loginUserName = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        loginPassword = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')

        loginUserName.send_keys(self.userName)
        loginPassword.send_keys(self.password)
        time.sleep(1)
        loginPassword.send_keys(Keys.ENTER)


instagram = Instagram(userName,password)

instagram.logIn()



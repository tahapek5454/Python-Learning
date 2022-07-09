

from selenium import webdriver
import time


class Github:

    def __init__(self,user_name,password) -> None:

        self.user_name = user_name
        self.password = password
        self.driver = webdriver.Chrome(r"C:\Users\90543\Desktop\VS\python\web-driver\chromedriver.exe")
        self.followers = []

    def logIn(self):

        self.driver.get("https://github.com/login")

        self.driver.find_element_by_xpath('//*[@id="login_field"]').send_keys(self.user_name)
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(self.password)
        
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="login"]/div[4]/form/div/input[12]').click()

    def getFollowers(self):

        self.driver.get(f"https://github.com/{self.user_name}?tab=followers")

        elemnts = self.driver.find_elements_by_css_selector('.d-table.table-fixed')

        for i in elemnts:
            self.followers.append(i.find_element_by_css_selector('.f4.Link--primary').text)
        
        while True:
            links = self.driver.find_element_by_class_name('paginate-container').find_elements_by_tag_name('a')

            if len(links)!=0:
                # sonraki sayfalar vardir
                for i in links:
                    if i.text == 'Next':
                        i.click()
                        time.sleep(1)
                        elemnts = self.driver.find_elements_by_css_selector('.d-table.table-fixed')
                        for i in elemnts:
                            self.followers.append(i.find_element_by_css_selector('.f4.Link--primary').text)
                
                
            else:
                
                break
        
        for i in self.followers:
            print(i)


github = Github('YourUserName','YourPassword')

github.logIn()
print('*'*100)
github.getFollowers()
print('*'*100)

        

    
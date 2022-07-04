
from unittest import result
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

driver = webdriver.Chrome()

url = "http://github.com"
driver.get(url)

searchInput = driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div[2]/div[1]/div/div/form/label/input[1]")
#time.sleep(1)

searchInput.send_keys("python")
#time.sleep(1)

searchInput.send_keys(Keys.ENTER)

#time.sleep(2)

result = driver.find_elements_by_xpath('/html/body/div[4]/main/div/div[3]/div/ul/li[1]/div[2]/div[1]/div[1]')

print("*"*100)
for item in result:
    print(item.text)
    print("-"*50)
print("*"*100)
driver.close()


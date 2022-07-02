
from selenium import webdriver
import time

driver = webdriver.Chrome()

url = "http://github.com"

driver.get(url)

print(driver.title)

driver.save_screenshot("ss.png")

time.sleep(2)

driver.maximize_window()

time.sleep(2)

url = "http://github.com/tahapek5454"

driver.get(url)

time.sleep(2)

driver.back()

time.sleep(1)

driver.forward()

driver.close()



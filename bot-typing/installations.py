
# pip install --user selenium

from selenium import webdriver

driver = webdriver.Chrome(r"C:\Users\90543\Desktop\VS\python\web-driver\chromedriver.exe")

url = "https://github.com/tahapek5454"

driver.get(url)
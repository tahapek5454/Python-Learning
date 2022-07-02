
# pip install --user selenium

from selenium import webdriver

driver = webdriver.Chrome()

url = "https://github.com/tahapek5454"

driver.get(url)
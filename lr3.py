from selenium import webdriver
from selenium.webdriver.common.by import By
import webbrowser
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

relevant = 0
addr = "Театральная"
body_text = []

def searchAddr():
    body = driver.find_element_by_tag_name("body")
    body_text = body.text
    global relevant
    if body_text.find(addr) != -1 :
        relevant += 1
        #print(relevant)
        
driver.get("https://www.google.com/")

search = driver.find_element_by_name('q')
search.send_keys("Большой театр")
search.send_keys(Keys.ENTER)

time.sleep(2)
results_list = []
results = driver.find_elements_by_class_name('r')

for result in results:
    print(result.find_element_by_tag_name("a").get_attribute("href"))
    results_list.append(result.find_element_by_tag_name("a").get_attribute("href"))

time.sleep(2)
driver.find_element_by_id("pnnext").click();
    
results = driver.find_elements_by_class_name('r')

for result in results:
    print(result.find_element_by_tag_name("a").get_attribute("href"))
    results_list.append(result.find_element_by_tag_name("a").get_attribute("href"))

for i in range(0, len(results_list)):
    driver.get(results_list[i])
    searchAddr()
    
print("Релевантных ссылок:")
print(relevant)

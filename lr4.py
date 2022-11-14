from selenium import webdriver
from selenium.webdriver.common.by import By
import webbrowser
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("https://sprungmarker.de/")

post_num = 0
post_list = []

cookies = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#BorlabsCookieBox > div > div > div > div.cookie-box > div > div > div > p:nth-child(4) > a"))).click()
content = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "main")))

posts = content.find_elements(By.TAG_NAME, "article")

for post in posts: 
    post_num += 1
    link = post.find_element(By.TAG_NAME, "a").get_attribute("href")
    print(link)
    post_list.append(link)

for link in post_list:
    driver.execute_script("window.open('');")              
    driver.switch_to.window(driver.window_handles[-1])     
    driver.get(link)  
    time.sleep(2)
    driver.close() 
    driver.switch_to.window(driver.window_handles[-1])

navigation = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#main > nav > div > a:nth-child(2)"))).click()
navigation = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#main > nav > div > a.next.page-numbers"))).click()

print("Количество постов на главной странице - "+ str(post_num))  
time.sleep(2)
driver.quit()

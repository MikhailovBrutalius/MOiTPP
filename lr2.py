from selenium import webdriver
import webbrowser
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

driver.get("https://www.artlebedev.ru/case/")

text = driver.find_element_by_id('source')
text.send_keys("kekus DOMINATUS")
ok = 0

time.sleep(5)

high = driver.find_element_by_link_text('ВЕРХНИЙ РЕГИСТР')
high.click()
time.sleep(2)
str = driver.find_element_by_id('target').get_attribute('value')
if str == "KEKUS DOMINATUS" :
    ok+=1

low = driver.find_element_by_link_text('нижний регистр')
low.click()
time.sleep(2)
str = driver.find_element_by_id('target').get_attribute('value')
if str == "kekus dominatus" :
    ok+=1
    
big = driver.find_element_by_link_text('Заглавные Буквы')
big.click()
time.sleep(2)
str = driver.find_element_by_id('target').get_attribute('value')
if str == "Kekus Dominatus" :
    ok+=1
    
firstBig = driver.find_element_by_link_text('Первая заглавная')
firstBig.click()
time.sleep(2)
str = driver.find_element_by_id('target').get_attribute('value')
if str == "Kekus dominatus" :
    ok+=1
    
inverse = driver.find_element_by_link_text('иНВЕРСИЯ рЕГИСТРА')
inverse.click()
time.sleep(2)
str = driver.find_element_by_id('target').get_attribute('value')
if str == "KEKUS dominatus" :
    ok+=1
    
about = driver.find_element_by_link_text('О программе')
about.click()
time.sleep(2)

if ok == 5 :
    print("Тест пройден успешно")
else :
    print("Тест не пройден")

from selenium import webdriver
import webbrowser
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()                                    #инициализация браузера

driver.get("https://www.artlebedev.ru/case/")                   #открытие сайта в браузере

text = driver.find_element(By.NAME, 'source')                   #нахождение поля для входного текста 
text.send_keys("test. LINE")                                    #запись тестовой строки
ok = 0                                                          #счётчик успешно пройденных проверок

time.sleep(2)

high = driver.find_element(By.XPATH, '//a[text()="ВЕРХНИЙ РЕГИСТР"]')       #нахождение кнопки верхнего регистра
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")    #прокрутка вниз 
driver.execute_script("arguments[0].click();", high)                        #клик 
time.sleep(1)
str = driver.find_element(By.ID, 'target').get_attribute('value')           #получение выходной строки
if str == "TEST. LINE" :                                                    #проверка правильности конвертации 
    ok+=1
    print(str)

low  = driver.find_element(By.XPATH, '//a[text()="нижний регистр"]')        #нахождение кнопки нижнего регистра
low.click()
time.sleep(1)
str = driver.find_element(By.ID, 'target').get_attribute('value')
if str == "test. line" :
    ok+=1
    print(str)
    
big  = driver.find_element(By.XPATH, '//a[text()="Заглавные Буквы"]')       #нахождение кнопки заглавных букв
big.click()
time.sleep(1)
str = driver.find_element(By.ID, 'target').get_attribute('value')
if str == "Test. Line" :
    ok+=1
    print(str)
    
    
inverse  = driver.find_element(By.XPATH, '//a[text()="иНВЕРСИЯ рЕГИСТРА"]') #нахождение кнопки инверсии регистра
inverse.click()
time.sleep(1)
str = driver.find_element(By.ID, 'target').get_attribute('value')
if str == "TEST. line" :
    ok+=1
    print(str)
    
firstBig  = driver.find_element(By.XPATH, '//a[text()="По предложениям"]')  #нахождение кнопки заглавных букв по предложениям
firstBig.click()
time.sleep(1)
str = driver.find_element(By.ID, 'target').get_attribute('value')
if str == "Test. LINE" :
    ok+=1
    print(str)

if ok == 5 :                                                                #если все 5 функций успешно сработали, 
    print("Тест пройден успешно")
else :
    print("Тест не пройден")

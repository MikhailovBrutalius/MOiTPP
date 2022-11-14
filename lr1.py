from selenium import webdriver
import webbrowser
import random
import time

browser = webdriver.Firefox()                               #инициализация браузера

file = open('D:\Myotipp\lr1\list.txt', 'r')                 #открытие файла со списком сайтов на чтение 

list1 = file.readlines()                                    #считывание списка
size = len(list1)                                           #размер списка 
list2 = []                                                  #новый список 2 для записи адресов в рандомизированном порядке

for i in range(0, size):
    rndLine = random.choice(list1)                          #выбирает случайный сайт из списка
    browser.execute_script("window.open('');")              #открытие новой вкладки
    browser.switch_to.window(browser.window_handles[-1])    #переход на новую вкладку (крайнюю справа)
    browser.get(rndLine)                                    #октрытие сайта на открытой вкладке
    list1.remove(rndLine)                                   #удаление адреса открытого сайта из списка 1
    list2.append(rndLine)                                   #занесение адреса в новый список 2 

file = open('D:\Myotipp\lr1\list.txt', 'w')                 #открытие файла со списком сайтов на запись
time.sleep(1)

for i in range(0,size):                                     
    file.write(list2[i])                                    #запись в файл адреса в новом (случайном) порядке
    browser.close()                                         #закрытие вкладки
    browser.switch_to.window(browser.window_handles[-1])    #переход на следующую вкладку (крайнюю справа) 
    time.sleep(1)
      
file.close()                                                #закрытие файла 
print("end")



















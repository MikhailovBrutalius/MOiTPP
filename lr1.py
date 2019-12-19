from selenium import webdriver
import webbrowser
import random
import time
#
browser = webdriver.Firefox()

f = open('F:\_Outchjoobeescthe\Myotipp\lr1\list.txt', 'r')

list1 = f.readlines()
siez = len(list1)
list2 = []

for i in range(0, siez):
    rndLine = random.choice(list1)
    browser.execute_script("window.open('');")
    browser.switch_to.window(browser.window_handles[-1])
    browser.get(rndLine)
    list1.remove(rndLine)
    list2.append(rndLine)

f = open('F:\_Outchjoobeescthe\Myotipp\lr1\list.txt', 'w')
time.sleep(1)

for i in range(0,siez):
    f.write(list2[i])
    browser.close()
    browser.switch_to.window(browser.window_handles[-1])
    time.sleep(1)
      
f.close()
print("end")















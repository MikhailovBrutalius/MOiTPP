from selenium import webdriver
from selenium.webdriver.common.by import By
import webbrowser
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def getResults():               #функция обнаружения результатов поискового запроса (ссылок) на странице и их записи в список
    global results_list
    content = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "b_content")))     
    results = content.find_elements(By.CLASS_NAME, "b_algo")
    for result in results:
        link = result.find_element(By.TAG_NAME, "a").get_attribute("href")
        results_list.append(link)

def searchAddr(url):            #функция поиска вхождений искомого адреса в тексте html-источника страницы  
    driver.get(url)
    body_text = driver.page_source
    global relevant
    if body_text.find("Театральная" or "Theatre square" or "Teatralnaya") != -1 :
        relevant += 1
        print(url + " - релевантная ссылка")
    else :
        print(url)

driver = webdriver.Firefox()
driver.get("https://www.bing.com/")
relevant = 0
results_list=[]

search = driver.find_element(By.NAME, 'q')
search.send_keys("Большой театр")
search.send_keys(Keys.ENTER)
time.sleep(2)

getResults()

next_page=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#b_results > li.b_pag > nav > ul > li:last-child")))
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
next_page.click()

getResults()

for result in results_list:
    searchAddr(result)

print('Релевантных ссылок: ' + str(relevant))
driver.quit()



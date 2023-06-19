#Made by https://github.com/0MeMo07/

import time
import os
import pwinput
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


os.system('cls' if os.name == 'nt' else 'clear')
email = input("Linkedin email ->")
password = pwinput.pwinput("Linkedin password ->")
keywords = input("keywords ->")
os.system('cls' if os.name == 'nt' else 'clear')

#If you want to configure Chrome options for headless mode, you can uncomment the lines by removing the '#' symbols in the code.
#chrome_options = Options()
#chrome_options.add_argument("--headless")
#chrome_options.add_argument("--no-sandbox")  
#chrome_options.add_argument("--disable-dev-shm-usage") 
#driver = webdriver.Chrome(options=chrome_options)

driver = webdriver.Chrome()

driver.get("https://www.linkedin.com/uas/login")
driver.find_element(By.ID, 'username').send_keys(f'{email}')
word = driver.find_element(By.ID, 'password')
word.send_keys(f'{password}')
word.submit()
time.sleep(6)

keywords = f"{keywords}"


for page in range(100):
    url = "https://www.linkedin.com/search/results/people/?keywords=" + keywords + "&origin=CLUSTER_EXPANSION&page=" + str(page)
    driver.get(url)
    time.sleep(1)
    for index in range(10):
        try:
            connections = driver.find_element(By.XPATH, f'/html/body/div[5]/div[3]/div[2]/div/div[1]/main/div/div/div[2]/div/ul/li[{index}]/div/div/div[3]/div/button')
            index +=1
            print(index)
            connections.click()
            time.sleep(0.5)
            connection_button = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/button[2]")
            connection_button.click()
            time.sleep(0.5)
        except:
            print('Button Not now not found')
            pass
    time.sleep(2)

driver.quit()
    

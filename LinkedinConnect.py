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
pages = 200  

index = 0
for page in range(1, pages + 1):
    url = "https://www.linkedin.com/search/results/people/?keywords=" + keywords + "&origin=CLUSTER_EXPANSION&page=" + str(page)
    driver.get(url)
    index=0
    time.sleep(2)

    while True:
        try:
            connections = driver.find_elements(By.XPATH, f'/html/body/div[5]/div[3]/div[2]/div/div[1]/main/div/div/div[2]/div/ul/li[{index+1}]/div/div/div[3]/div/button')
            time.sleep(2)
            if not connections:
                print('No more buttons found on the page.')
                break

            for connection in connections:
                try:
                    if connection.get_attribute("xpath") == '/html/body/div[4]/div[3]/div[2]/div/div[1]/main/div/div/div[2]/div/ul/li[9]/div/div/div[3]/div/div/button':
                        pass
                        continue
                    connection.click()
                    time.sleep(1)

                    connection_button = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/button[2]")
                    connection_button.click()
                    time.sleep(1)
                except:
                    print('Button Not now not found')
                    pass
            
            index += 1
        except:
            print('Error occurred while processing buttons.')
            break

    time.sleep(2)

driver.quit()

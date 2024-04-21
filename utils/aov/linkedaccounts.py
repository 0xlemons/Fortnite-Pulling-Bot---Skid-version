from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

def findepic(username):
    try:
        options = uc.ChromeOptions()
        options.add_argument("--incognito") 
        #options.add_argument("--headless=new")
        options.add_argument("--window-size=10,10")
        options.add_argument('--disable-gpu') 
        driver = uc.Chrome(options=options)
        url = "https://fortnitetracker.com" 
        driver.get(url)
        input_element = driver.find_element(By.NAME, "q") 
        input_element.send_keys(username)
        input_element.submit()
        current_url = driver.current_url
        last_segment = current_url.split("/")[-1]
        print("Epic username:", last_segment)
        driver.quit()
        return(last_segment)

    except:
        
        driver.quit()
        return None


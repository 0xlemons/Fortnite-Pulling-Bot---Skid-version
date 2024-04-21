import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup

def fried(username):
    options = uc.ChromeOptions()
    options.add_argument("--incognito") 
    options.add_argument("--window-size=10,10")
    options.add_argument('--disable-gpu') 
    driver = uc.Chrome(options=options)
   
    

    
    driver.get(f'https://gamerdvr.com/gamer/{username}')
    page_source = driver.page_source

    soup = BeautifulSoup(page_source, "html.parser")

    elements = soup.find_all(class_="text-right")

    if len(elements) >= 2:
        second_element = elements[2]

        i_tag = second_element.find("i")
        if i_tag:
            extracted_text = i_tag.text.strip()
            print(f"The extracted text from the second element is: {extracted_text}")
        else:
            print("The <i> tag was not found in the second element.")
    else:
        print("There are fewer than two elements with the specified class.")

    driver.quit()
    #followers = xboxinfo.followers(username)
    views = extracted_text
    if views:
        if int(views) > 15:
            return f' Yes | High Views ({views})'
        else:
            return None
           

    '''
    if vfriend and ffriend == True:            
        fried_reason = f' Yes | High Followers ({followers}) & High Views ({views})'
    elif vfriend == True:
        fried_reason = f' Yes | High Views ({views})'
    elif ffriend == True:
        fried_reason = f' Yes | High Followers ({followers})'
    else:
        fried_reason = 'No'
    '''
    

    



    


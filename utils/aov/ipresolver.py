import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from selenium.webdriver.common.keys import Keys
import time
import requests
import zipfile

def proxies(username, password, endpoint, port):
    manifest_json = """
    {
        "version": "1.0.0",
        "manifest_version": 2,
        "name": "Proxies",
        "permissions": [
            "proxy",
            "tabs",
            "unlimitedStorage",
            "storage",
            "<all_urls>",
            "webRequest",
            "webRequestBlocking"
        ],
        "background": {
            "scripts": ["background.js"]
        },
        "minimum_chrome_version":"22.0.0"
    }
    """

    background_js = """
    var config = {
            mode: "fixed_servers",
            rules: {
              singleProxy: {
                scheme: "http",
                host: "%s",
                port: parseInt(%s)
              },
              bypassList: ["localhost"]
            }
          };

    chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

    function callbackFn(details) {
        return {
            authCredentials: {
                username: "%s",
                password: "%s"
            }
        };
    }

    chrome.webRequest.onAuthRequired.addListener(
                callbackFn,
                {urls: ["<all_urls>"]},
                ['blocking']
    );
    """ % (endpoint, port, username, password)

    extension = 'proxies_extension.zip'

    with zipfile.ZipFile(extension, 'w') as zp:
        zp.writestr("manifest.json", manifest_json)
        zp.writestr("background.js", background_js)

    return extension

username = ''
password = ''
endpoint = ''
port = ''




url = "https://xresolver.com/xbox"

def resolve(username):
    proxies_extension = proxies(username, password, endpoint, port)
    options = uc.ChromeOptions()
    options.add_argument("--incognito") 
    #opions.add_argument("--headless=new")
    options.add_argument('--disable-gpu')
    options.add_argument("--window-size=10,10") 
    options.add_extension(proxies_extension)
    driver = uc.Chrome(options=options)
    wait = WebDriverWait(driver, 10)
    driver.get('https://www.ipinfo.io/ip')
    time.sleep(3)
    driver.get(url)

    time.sleep(11)
    closebutton = wait.until(EC.presence_of_element_located((By.ID, "modalAdCloseBtn")))

    closebutton.click()

    input_box = wait.until(EC.presence_of_element_located((By.ID, "input")))

    input_box.send_keys(username)

    button = wait.until(EC.presence_of_element_located((By.ID, "button")))

    button.click()
    time.sleep(2)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    page_source = driver.page_source

    ip_pattern = re.compile(r"\b(?!8\.8\.8\.8\b)\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b")
    try:
        ip_addresses = ip_pattern.findall(page_source)
        for ip_address in ip_addresses:
            print(f"Found IP Address: {ip_address}")
            driver.quit()
            return ip_address 
    except:
        print ("Ip not found")
        driver.quit()
        return None
    
    




    
    


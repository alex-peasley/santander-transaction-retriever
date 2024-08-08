import os
from os.path import join, dirname
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

PID = os.environ.get('PID')
SECURITY_NUMBER = os.environ.get('SECURITY_NUMBER')

browser = webdriver.Firefox()
browser.implicitly_wait(100)
browser.get('https://retail.santander.co.uk/olb/app/logon/access/#/logon')

try:
    # Clear cookie messages and banners
    accept_cookies = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler'))
    )
    app_ad = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, 'splash-97123-close-button'))
    ) 
    pid = browser.find_element(By.ID, 'pid')
    security_number =browser.find_element(By.ID, 'securityNumber')
    submit =browser.find_element(By.ID, 'submitbtn')
    
    ActionChains(browser) \
        .move_to_element(accept_cookies).click() \
        .move_to_element(app_ad).pause(2).click() \
        .move_to_element(pid).click().send_keys(PID) \
        .move_to_element(security_number).click().send_keys(SECURITY_NUMBER) \
        .move_to_element(submit).click() \
        .perform()
    
finally:
    # browser.quit()
    pass
import os
from os.path import join, dirname
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

PID = os.environ.get('PID')
SECURITY_NUMBER = os.environ.get('SECURITY_NUMBER')

options = FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)
driver.get('https://retail.santander.co.uk/olb/app/logon/access/#/logon')

try:
    # Clear cookie messages and banners
    accept_cookies = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler'))
    )
    app_ad = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'splash-97123-close-button'))
    ) 
    pid = driver.find_element(By.ID, 'pid')
    security_number =driver.find_element(By.ID, 'securityNumber')
    submit =driver.find_element(By.ID, 'submitbtn')
    
    ActionChains(driver) \
        .move_to_element(accept_cookies).click() \
        .move_to_element(app_ad).pause(2).click() \
        .move_to_element(pid).click().send_keys(PID) \
        .move_to_element(security_number).click().send_keys(SECURITY_NUMBER) \
        .move_to_element(submit).click() \
        .perform()
    
finally:
    # browser.quit()
    pass
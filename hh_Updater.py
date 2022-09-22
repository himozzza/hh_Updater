from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import os

def initialization():
    global driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.headless = False
    os.environ['WDM_LOG_LEVEL'] = '0'
    os.environ['WDM_LOG'] = '0'
    os.environ['IS_MINIMIZED'] = '1'
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--disable-plugins')
    chrome_options.add_argument('--guets')
    chrome_options.add_argument('--disable-images')
    chrome_options.add_argument('--disable-logging')
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument("--log-level=3")
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))
    driver.get('https://hh.ru/applicant/resumes?hhtmFromLabel=header&hhtmFrom=main')

def Main(login, password):
    initialization()
    
    ActionChains(driver).move_to_element(driver.find_element(By.XPATH, '//*[@data-qa="expand-login-by-password"]')).click().perform()
    ActionChains(driver).move_to_element(driver.find_element(By.XPATH, '//*[@class="bloko-input-text-wrapper"]')).click().send_keys(login).perform()
    ActionChains(driver).move_to_element(driver.find_element(By.XPATH, '//*[@data-qa="login-input-password"]')).click().send_keys(password, Keys.ENTER).perform()
    sleep(5)
    buttonsArr = driver.find_elements(By.XPATH, '//button[@data-qa="resume-update-button_actions"]')
    try:
        for button in buttonsArr:
            if (button.accessible_name == "Поднять в поиске"):
                ActionChains(driver).move_to_element(button).click().perform()
                print("Resume was updated.")
            else:
                print("Resume already updated.")
    except:
        print("All resumes was upped. Closing...")
    driver.quit()
        
Main(login="Your login in hh.ru", password="Your password in hh.ru")
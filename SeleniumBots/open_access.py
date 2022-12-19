import os, time
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def url_I_access(driver, op):

    load_dotenv()
    url = os.environ.get('URL_I')
    user = os.environ.get(f'USER_I_{op}')
    pword = os.environ.get(f'PASS_I_{op}')

    driver.get(url)
    driver.maximize_window()

    time.sleep(1)

    driver.find_element(By.NAME, 'email').send_keys(user)
    driver.find_element(By.NAME, 'senha').send_keys(pword)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'entrar'))).click()
    
    if WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'resp'))):
        try: WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'entrar'))).click()
        except: pass

def url_O_access(driver):

    load_dotenv()
    url = os.environ.get('URL_O')
    user = os.environ.get('USER_O')
    pword = os.environ.get('PASS_O')

    driver.get(url)
    driver.maximize_window()

    time.sleep(1)

    driver.find_element(By.NAME, 'username').send_keys(user)
    driver.find_element(By.NAME, 'password').send_keys(pword)
    driver.find_element(By.ID, 'btn_login').click()

    try: WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div/div/div/div[4]/button[2]'))).click()
    except: pass

def transfer_attendaces(customer_qtd, attendant=False, message=False, logoff=False, secs=0.7):

    import time, os
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import SeleniumBots.open_access as OpenAccess

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(options=options)

    OpenAccess.url_O_access(driver)

    # attendant = True
    # message = True
    # logoff = True

    try:

        time.sleep(secs*3)

        for customer_qtd in range(int(customer_qtd)):

            ## Balãozinho
            time.sleep(secs)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[4]/div[5]'))).click()

            ## Primeiro
            time.sleep(secs)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[5]/div[2]/div[2]'))).click()

            if message:

                ## Mensagem
                time.sleep(secs)
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[6]/div[1]/div[3]/div[1]/div[2]'))).send_keys('Estarei transferindo o atendimento para o nosso próximo atendente para darmos continuidade à sua tratativa. Nosso atendimento de Suporte Técnico Remoto agora é *24 horas*!')

                ## Enviar
                time.sleep(secs)
                driver.find_element(By.XPATH, '/html/body/div/div[6]/div[1]/div[3]/div[1]/div[2]').send_keys(Keys.ENTER)

            ## Transferir 1
            time.sleep(secs)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[6]/div[2]/div[20]/button[2]'))).click()

            ## Suporte
            time.sleep(secs)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[2]/form/div[2]/div[2]/select/option[7]'))).click()

            if attendant:

                ## Atendente
                time.sleep(secs)
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[2]/form/div[2]/div[3]/select/option[8]'))).click()

            ## Transferir 2
            time.sleep(secs)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[2]/form/div[1]/button'))).click()

            if attendant:

                ## OK
                time.sleep(secs)
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/div/div/div/div/div/div/div/div[4]/button[2]'))).click()

    except Exception as err:

        print(f'\n{err}\n')

    finally:
        
        if logoff:
                
            ## Logoff
            os.system('shutdown /l')

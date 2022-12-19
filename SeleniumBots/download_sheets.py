def download_sheets(op, date, test=False, secs=1.0):

    import time, os
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    if not test:
        import SeleniumBots.open_access as OpenAccess
    else:
        import open_access as OpenAccess

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(options=options)

    try:
        for file in ['relatorio', 'relatorio (1)', 'relatorio (2)']:
            os.remove(f'../{file}.xlsx')
    except: pass

    OpenAccess.url_I_access(driver, op)

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    ## Abrir Cadastro
    time.sleep(secs)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Cadastros"]'))).click()

    ## Abrir Clientes
    time.sleep(secs)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Clientes"]'))).click()

    ## Icone Download
    time.sleep(secs)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//i[@class="fa fa-download"]'))).click()

    ## Baixar Clientes
    time.sleep(secs)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//i[@class="fa fa-file-excel-o"]'))).click()

    # Fechar Cadastros
    time.sleep(secs)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Cadastros"]'))).click()

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    ## Abrir Provedor
    time.sleep(secs)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Provedor"]'))).click()

    ## Abrir Logins
    time.sleep(secs)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Logins"]'))).click()

    ## Icone Download
    time.sleep(secs)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//i[@class="fa fa-download"]'))).click()

    ## Baixar Logins
    time.sleep(secs)
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//i[@class="fa fa-file-excel-o"]'))).click()

    ## Fechar Provedor
    time.sleep(secs)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Provedor"]'))).click()

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    ## Abrir Suporte
    time.sleep(secs)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Suporte"]'))).click()

    ## Abrir Ordem de Serviço
    time.sleep(secs)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Ordem de Serviço"]'))).click()

    ## Desmarcar Abertos
    time.sleep(secs)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'Status_A'))).click()

    ## Desmarcar Encaminhados
    time.sleep(secs)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'Status_EN'))).click()

    ## Selecionar Data Inicial
    time.sleep(secs)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'data1'))).click()
    # time.sleep(secs)
    # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'data1'))).click()
    time.sleep(secs)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'data1'))).send_keys(date)

    ## Selecionar Data Final
    time.sleep(secs)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'data2'))).click()
    # time.sleep(secs)
    # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'data2'))).click()
    time.sleep(secs)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'data2'))).send_keys(date)

    ## Selecionar Filtro
    time.sleep(secs)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[3]/table/tbody/tr/td[5]/div[1]/input[1]'))).click()

    ## Icone Download
    time.sleep(secs)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//i[@class="fa fa-download"]'))).click()

    ## Baixar Serviços
    time.sleep(secs)
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//i[@class="fa fa-file-excel-o"]'))).click()

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    ## Logout
    time.sleep(secs)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/i'))).click()

    for file in ['relatorio', 'relatorio (1)', 'relatorio (2)']:
        os.replace(f'../../{file}.xlsx', f'../{file}.xlsx')

    time.sleep(secs*3)

    driver.close()

    return 'Planilhas baixadas com sucesso!'


# download_sheets('0', '25/11/2022', True)
import time, re, traceback
from datetime import datetime
import pandas as pd

from SeleniumCore import By, Keys
from SeleniumCore import get_wait, get_actions, located

from Search_Register import Search_Register as SEARCH
from register_infos import Register_Infos as INFOS

class Emergency:

    def __init__(self, driver):

        self.driver = driver
        self.wait = get_wait(self.driver)
        self.actions = get_actions(self.driver)

        self.current_date = datetime.now()
        self.info = '\033[36m'

    def format_phone(self, phone):

        phone = ''.join(re.findall('[0-9]+', phone))
        if (len(phone) > 10):
            return f'({phone[:2]}) {phone[2:7]}-{phone[7:11]}'
        elif (len(phone) > 9):
            return f'({phone[:2]}) {phone[2:6]}-{phone[6:10]}'
        else:
            return phone

    def generate_emergency(self, option, name, condominium, block, apt, complement, phone, login, band, current_date):

        emergency = open(f'../chamado__{name}.txt', 'w')

        subject = 'Visita Técnica' if option == 't' else 'Retirada de Equipamentos'
        phone = self.format_phone(phone)

        if option == 't':
            description = 'Cliente sem conexão. Los piscando vermelho e Pon apagada na Onu.' + '\n' + login + ' - ' + band
        else:
            description = 'Retirar n'

        emergency.write(f'*{subject} - {current_date}*\n{name}\n{condominium} - Bloco {block.zfill(2)} - Apto {apt.zfill(2)}\n{phone}\n{description}')

        emergency.close()

    def register_infos(self, df_register, option):

        condominium_list = pd.read_excel('sheets/Condominiums.xlsx', sheet_name='Condomínios')

        df_register['Cond_Code'] = df_register['Cond_Code'].astype(str)
        condominium_list['Cond_Code'] = condominium_list['Cond_Code'].astype(str)

        infos = pd.merge(df_register, condominium_list, on='Cond_Code')
        infos.drop('Cond_Code', axis=1, inplace=True)

        for _, row in infos.iterrows():

            name = row['Register_Name']
            condominium = row['Condominium']
            block = str(row['Block'])
            apt = str(row['Apt'])
            complement = str(row['Complement'])
            phone = str(row['Phone'])
            login = row['Login']
            band = row['Band'].split('_')[0]

            current_day = self.current_date.day
            current_month = self.current_date.month

            current_date = str(current_day).zfill(2) + '/' + str(current_month).zfill(2)

            self.generate_emergency(option, name, condominium, block, apt, complement, phone, login, band, current_date)

            register_name = name

            break

        return register_name

    def register_verify(self, type, register_id, service):
    
        try:

            ## Search
            registers = self.wait.until(located((By.XPATH, '/html/body/div[1]/div[3]/div/div[1]/div[2]/ul/li[1]/a')))
            self.driver.execute_script('arguments[0].click();', registers)

            SEARCH.open_register_search(self, type, register_id)

            data = [INFOS.get_register_infos(self, '2')]

            df_register = pd.DataFrame(data, columns=['Register_Name', 'Cond_Code', 'Block', 'Apt', 'Complement', 'District', 'Phone', 'Login', 'Band'])

            time.sleep(1)
            for _ in range(2): get_actions(self.driver).send_keys(Keys.ESCAPE).perform()

            register = self.register_infos(df_register, service)

            time.sleep(1)
            for _ in range(4): get_actions(self.driver).send_keys(Keys.ESCAPE).perform()

            return ['success', ' Emergency service generated for: ' + self.info + register]
    
        except:

            return ['error', traceback.format_exc()]


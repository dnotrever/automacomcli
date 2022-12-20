import pandas as pd

condominiums = pd.read_excel('Sheets/Condominiums_List.xlsx', sheet_name='Condomínios')

customers_list = pd.read_excel("../relatorio.xlsx")
logins_list = pd.read_excel("../relatorio (1).xlsx")
services_list = pd.read_excel("../relatorio (2).xlsx")

#--- Tests ---#
# customers_list = pd.read_excel("Sheets/Tests/Customers_Test.xlsx")
# services_list = pd.read_excel("Sheets/Testes/Services_Test.xlsx")

customers = customers_list.loc[:,[
    'ID',
    'Razão social', 
    'Condomínio', 
    'Bloco', 
    'Apartamento', 
    'Telefone celular', 
    'Hotsite email',
    'Complemento']]

customers.rename(columns={
    'Razão social': 'Cliente',
    'Condomínio': 'CondNotForm',
    'Bloco': 'Bl',
    'Apartamento': 'Apto',
    'Telefone celular': 'Celular',
    'Hotsite email': 'App User'},
    inplace=True)

logins = logins_list.loc[:,[
    'Cliente', 
    'Login',
    'Contrato']]

services = services_list.loc[:,[
    'Cliente', 
    'Assunto', 
    'Mensagem',
    'Horário']]

incomplete_registrations = pd.merge(customers, condominiums, on='CondNotForm')

registrations = pd.merge(incomplete_registrations, logins, on='Cliente')
registrations.drop('CondNotForm', axis=1, inplace=True)

partial_services = pd.merge(registrations, services, on='Cliente')

total_services = pd.merge(incomplete_registrations, services, on='Cliente')

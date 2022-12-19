import helpers, os

def register_customer(subject, name, condominium, block, apt, cell, description, login, band, complement, tomorrow_date, services):

    if subject in helpers.PlanSubjects['migration']:
        services.write('\n*Migração para Fibra - ')

    elif subject in helpers.PlanSubjects['equip-change']:
        services.write('\n*Troca do Roteador - ')

    elif subject == 'Retirada de Equipamentos':
        services.write('\n*Retirada de Equipamento - ')
        
    else:
        services.write('\n*Visita Técnica - ')

    services.write('{}*\n{}\n{} \n{} \n'
        .format(
            tomorrow_date,
            name,
            helpers.format_block(block, apt, condominium, complement),
            helpers.format_cell(cell)
        ))

    if subject != 'Retirada de Equipamentos':
        services.write('{}\n{} - {}\n'.format(description, login, band))
    else:
        first_row = description.split('\n')
        services.write('{}\n'.format(first_row[0]))

def generate_services():

    import config

    services = open('../Lista_Chamados.txt', 'w')

    cont = 0

    for _, row in config.partial_services.iterrows():

        colunas = [
            row['Assunto'], 
            row['Cliente'], 
            row['Condomínio'], 
            str(row['Bl']), 
            str(row['Apto']), 
            str(row['Celular']), 
            row['Mensagem'], 
            row['Login'], 
            row['Contrato'],
            row['Complemento'],
        ]

        subject, name, condominium, block, apt, cell, description, login, contract, complement = colunas

        band = str(contract).split('_')[0]

        tomorrow_date = '{}/{}'.format(helpers.tomorrow_day, helpers.tomorrow_month)

        if subject != 'Instalação':
            register_customer(subject, name, condominium, block, apt, cell, description, login, band, complement, tomorrow_date, services)
            cont += 1
    
    services.close()

    for file in ['relatorio', 'relatorio (1)', 'relatorio (2)']:
        os.remove(f'../{file}.xlsx')

    return f'{cont} Chamados Gerados!'

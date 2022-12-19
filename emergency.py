import helpers

def register_service(option, name, condominium, block, apt, cell, login, complement, band, current_date):

    emergency_service = open(f'../Chamado__{name}.txt', 'w')

    if option == 'c':
        emergency_service.write('*Visita Técnica - ')
    
    if option == 'r':
        emergency_service.write('*Retirada de Equipamentos - ')

    emergency_service.write('{}*\n{}\n{} \n{} \n'
        .format(
            current_date,
            name,
            helpers.format_block(block, apt, condominium, complement),
            helpers.format_cell(cell)
        ))

    if option == 'c':
        emergency_service.write('Cliente sem conexão. Los piscando vermelho e Pon pagada na Onu. \n{} - {}\n'.format(login, band))

def generate_emergency_services(option, id):

    import config

    success_valid = False

    for _, row in config.registrations.iterrows():

        columns = [
            str(row['ID']),
            row['Cliente'],
            row['Condomínio'],
            str(row['Bl']),
            str(row['Apto']),
            str(row['Celular']),
            row['Login'],
            row['Contrato'],
            row['Complemento'],
        ]

        customer_id, name, condominium, block, apt, cell, login, contract, complement = columns

        band = str(contract).split('_')[0]

        current_date = '{}/{}'.format(helpers.current_day, helpers.current_month)

        if id.replace(' ','') == customer_id:
            register_service(option, name, condominium, block, apt, cell, login, complement, band, current_date)
            success_valid = True
            customer_name = name
            if option == 'c':
                subject = 'de Conexão'
            if option == 'r':
                subject = 'de Retirada'

    if success_valid:
        return f'Chamado {subject} gerado para {customer_name}!'
    else:
        return 'Cliente não encontrado!'

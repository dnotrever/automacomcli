def register_ending_services():

    import config

    endings = open('../Customers_Services.txt', 'w')

    for _, row in config.total_services.iterrows():

        columns = [
            row['Cliente'],
            row['Assunto'],
        ]

        customer, subject = columns

        if subject != 'Instalação':
            endings.write(f'{customer}\n')

    endings.close()

    return 'Clientes para Finalização listados com sucesso!'

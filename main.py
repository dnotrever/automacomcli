from os import system

system('mode con: cols=125 lines=25')

try:

    import helpers, emergency, services, logins, provisioning, endings, schedulings

    from SeleniumBots import register_logins as RL
    from SeleniumBots import download_sheets as DS
    from SeleniumBots import os_scheduling as OS
    from SeleniumBots import os_completion as OE
    from SeleniumBots import close_attendance as CA
    from SeleniumBots import contract_activation as IN

except Exception as err:

    print(f'\n  >> An Error has occured!\n\t{err}\n')
    option = input('\tInsert 0 to close terminal: ')
    if option == '0': system('exit')

else:

    others, success, error, info, reset = helpers.MessagesColors.values()

    historic = []

    def command_line():

        arr_command = []
        command = input('\n  $~ ')
        arr_command = command.split()

        if arr_len(arr_command, 0):
                
            if arr_command[0] == 'ac':

                if arr_len(arr_command, 1):
                    
                    if arr_command[1] == 'emerg':

                        if arr_len(arr_command, 2):

                            if arr_command[2] == 'c' or arr_command[2] == 'r':

                                opt = arr_command[2]

                                if arr_len(arr_command, 3):

                                    if arr_command[3] == '?':
                                        print(f'\n  >>{info} Parâmetro: ID do Cliente{reset}')
                                        command_line()

                                    elif arr_command[3] != '':

                                        id = arr_command[3]

                                        if len(arr_command) < 5:

                                            try:
                                                msg = emergency.generate_emergency_services(opt, id)
                                                print(f'\n  >> {success}{msg}{reset}')
                                                historic.append(''.join(msg))

                                            except Exception as err:
                                                print(f'\n  >>{error} Ocorreu um erro...{reset}\t{info}\n    {err}{reset}')
                                                command_line()

                                            command_line()

                                        else: message(3)

                                    else: message(2)
                            
                                else: message(2)

                            elif arr_command[2] == '?':
                                print(f'\n  >>{info} Possíveis parâmetros: c (Problema de Conexão) | r (Retirada de Equipamentos){reset}')
                                command_line()

                            else: message(1)

                        else: message(2)

                    elif arr_command[1] == 'servs':

                        if arr_len(arr_command, 2):

                            if arr_command[2] != '?':

                                op = arr_command[2]

                                if arr_len(arr_command, 3):

                                    if arr_command[3] != '?':

                                        date = arr_command[3]

                                        if len(arr_command) < 5:

                                            try:
                                                msg1 = DS.download_sheets(op, date)
                                                print(f'\n  >> {success}{msg1}{reset}')

                                                msg2 = services.generate_services()
                                                print(f'\n  >> {success}{msg2}{reset}')

                                                historic.append(''.join(msg1))
                                                historic.append(''.join(msg2))

                                            except Exception as err:
                                                print(f'\n  >>{error} Ocorreu um erro...{reset}\t{info}\n    {err}{reset}')
                                                command_line()

                                            command_line()

                                        else: message(3)

                                    elif arr_command[3] == '?':
                                        print(f'\n  >>{info} Possíveis parâmetros: Data dos Serviços{reset}')
                                        command_line()

                                    else: message(1)

                                else: message(2)

                            elif arr_command[2] == '?':
                                print(f'\n  >>{info} Possíveis parâmetros: Código do Operador{reset}')
                                command_line()

                            else: message(1)

                        else: message(2)

                    elif arr_command[1] == 'logins':

                        if arr_len(arr_command, 2):

                            op = arr_command[2]

                            if op != '?':

                                if len(arr_command) < 4:

                                    try:
                                        msg1 = logins.generate_logins()
                                        print(f'\n  >> {success}{msg1}{reset}')

                                        msg2 = RL.register_logins(op)
                                        print(f'\n  >> {success}{msg2}{reset}')

                                        historic.append(''.join(msg1))
                                        historic.append(''.join(msg2))

                                    except Exception as err:
                                        print(f'\n  >>{error} Ocorreu um erro...{reset}\t{info}\n    {err}{reset}')
                                        command_line()

                                    command_line()

                                else: message(3)

                            elif arr_command[2] == '?':
                                print(f'\n  >>{info} Parâmetro: Código do Operador{reset}')
                                command_line()

                            else: message(1)

                        else: message(2)

                    elif arr_command[1] == 'provis':

                        if len(arr_command) < 3:

                            try:
                                msg = provisioning.generate_customers_info()
                                print(f'\n  >> {success}{msg}{reset}')
                                historic.append(''.join(msg))

                            except Exception as err:
                                print(f'\n  >>{error} Ocorreu um erro...{reset}\t{info}\n    {err}{reset}')
                                command_line()

                        else:

                            if len(arr_command) > 8:

                                if len(arr_command) < 11:

                                    try:
                                        infos = '{} {} {} {} {} {}'.format(arr_command[2], arr_command[3], arr_command[4], arr_command[5], arr_command[6], arr_command[7])
                                        msg1 = provisioning.generate_provisioning(infos)
                                        print(f'\n  >> {success}{msg1}{reset}')
                                        msg2 = IN.contract_activation(arr_command[8], arr_command[9])
                                        print(f'\n  >> {success}{msg2}{reset}')
                                        historic.append(''.join(msg2))

                                    except Exception as err:
                                        print(f'\n  >>{error} Ocorreu um erro...{reset}\t{info}\n    {err}{reset}')
                                        command_line()

                                else: message(3)

                            else: message(2)

                        command_line()

                    elif arr_command[1] == 'sheets':

                        if arr_len(arr_command, 2):

                            if arr_command[2] != '?':

                                op = arr_command[2]

                                if arr_len(arr_command, 3):

                                    if arr_command[3] != '?':

                                        if len(arr_command[3]) > 9:
                                        
                                            date = arr_command[3]

                                            if len(arr_command) < 5:

                                                try:
                                                    msg = DS.download_sheets(op, date)
                                                    print(f'\n  >> {success}{msg}{reset}')
                                                    historic.append(''.join(msg))

                                                except Exception as err:
                                                    print(f'\n  >>{error} Ocorreu um erro...{reset}\t{info}\n    {err}{reset}')
                                                    command_line()

                                                command_line()

                                            else: message(3)

                                        else: message(1)

                                    if arr_command[3] == '?':
                                        print(f'\n  >>{info} Parâmetro: Data da Planilha{reset}')
                                        command_line()
                                    
                                    else: message(2)

                                else: message(2)

                            if arr_command[2] == '?':
                                print(f'\n  >>{info} Parâmetro: Código do Operador{reset}')
                                command_line()

                            else: message(2)

                        else: message(2)

                    elif arr_command[1] == 'sched':

                        if arr_len(arr_command, 2):

                            op = arr_command[2]

                            if len(arr_command) < 4:

                                if op != '?' and op != '-l':

                                    try:
                                        msg = OS.os_scheduling(op)
                                        print(f'\n  >> {success}{msg}{reset}')
                                        historic.append(''.join(msg))

                                    except Exception as err:
                                        print(f'\n  >>{error} Ocorreu um erro...{reset}\t{info}\n    {err}{reset}')
                                        command_line()

                                    command_line()

                                elif op == '-l':

                                    try:
                                        msg = schedulings.register_customers_schedulings()
                                        print(f'\n  >> {success}{msg}{reset}')
                                        historic.append(''.join(msg))

                                    except Exception as err:
                                        print(f'\n  >>{error} Ocorreu um erro...{reset}\t{info}\n    {err}{reset}')
                                        command_line()

                                    command_line()

                                elif arr_command[2] == '?':
                                    print(f'\n  >>{info} Possíveis parâmetros: Código do Operador | -l (Clientes para Agendamentos){reset}')
                                    command_line()

                                else: message(1)

                            else: message(3)

                        else: message(2)

                    elif arr_command[1] == 'atend':

                        if arr_len(arr_command, 2):

                            if arr_command[2] != '?':

                                customer_qtd = arr_command[2]

                                if len(arr_command) < 4:

                                    try: CA.transfer_attendaces(customer_qtd)

                                    except Exception as err:
                                        print(f'\n  >>{error} Ocorreu um erro...{reset}\t{info}\n    {err}{reset}')
                                        command_line()

                                    command_line()

                                else: message(3)

                            elif arr_command[2] == '?':
                                print(f'\n  >>{info} Parâmetro: Número de Atendimentos{reset}')
                                command_line()

                            else: message(2)

                        else: message(2)

                    elif arr_command[1] == 'compl':

                        if arr_len(arr_command, 2):

                            op = arr_command[2]

                            if len(arr_command) < 4:

                                if op != '?' and op != '-l':

                                    try:
                                        msg = OE.os_completion(op)
                                        print(f'\n  >> {success}{msg}{reset}')
                                        historic.append(''.join(msg))

                                    except Exception as err:
                                        print(f'\n  >>{error} Ocorreu um erro...{reset}\t{info}\n    {err}{reset}')
                                        command_line()

                                    command_line()

                                elif op == '-l':

                                    try:
                                        msg = endings.register_ending_services()
                                        print(f'\n  >> {success}{msg}{reset}')
                                        historic.append(''.join(msg))

                                    except Exception as err:
                                        print(f'\n  >>{error} Ocorreu um erro...{reset}\t{info}\n    {err}{reset}')
                                        command_line()

                                    command_line()

                                elif arr_command[2] == '?':
                                    print(f'\n  >>{info} Possíveis parâmetros: Código do Operador | -l (Clientes para Finalização){reset}')
                                    command_line()

                                else: message(1)

                            else: message(3)

                        else: message(2)

                    elif arr_command[1] == '?':
                        print(f'\n  >>{info} Possíveis parâmetros: emerg | servs | logins | provis | sheets | sched | atend | compl {reset}')
                        command_line()

                    else: message(1)

                else: message(2)

            elif command == 'exit': return

            elif command == 'hist':

                if len(historic) == 0:
                    print(f'\n  >> {info}Não há histórico a ser exibido.{reset}')
                else:
                    for msg in historic:
                        print(f'\n     {info}{msg}{reset}')

                command_line()

            elif command == 'clear':
                system('cls')
                command_line()

            else: message(1)

        else: command_line()

    def message(msg):
        if msg == 1: print(f'\n  >> {error}Erro: Commando não reconhecido.{reset}')
        if msg == 2: print(f'\n  >> {error}Erro: Parâmetro faltando.{reset}')
        if msg == 3: print(f'\n  >> {error}Erro: Excesso de parâmetros.{reset}')
        command_line()

    def arr_len(arr, num):
        if len(arr) > num: return True

    command_line()

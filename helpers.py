import datetime, re, os
from datetime import date
from dotenv import load_dotenv

def format_block(block, apt, condominium, complement):
    if block != 'nan':
        block = ''.join(re.findall('[0-9]+', block))
        if len(block) == 1:
            return f'{condominium} - Bloco 0{block} - Apto {apt}'
        else:
            return f'{condominium} - Bloco {block} - Apto {apt}'
    else:
        return f'{condominium} - {complement.title()}'

def format_cell(cell):
    cell = ''.join(re.findall('[0-9]+', cell))
    if (len(cell) > 10):
        return f'({cell[:2]}) {cell[2:7]}-{cell[7:11]}'
    elif (len(cell) > 9):
        return f'({cell[:2]}) {cell[2:6]}-{cell[6:10]}'
    else:
        return cell

def time_service_region(arr_regiao, time, condominium, subject):
    if time == 'Manhã': arr_regiao.append([1, time, condominium, subject])
    if time == 'Tarde': arr_regiao.append([2, time, condominium, subject])
    if time == 'Qualquer': arr_regiao.append([3, time, condominium, subject])

MessagesColors = {
    'others': '\033[1;34m',
    'success': '\033[0;32m',
    'error': '\033[1;31m',
    'info': '\033[1;90m',
    'reset': '\033[0;0m',
}

PlanSubjects = {
    'migration': ['Migração de tecnologia e Upgrade de banda', 'Migração de Plano'],
    'equip-change': ['Upgrade de Velocidade', 'Downgrade de Velocidade', 'Troca de Roteador'],
}

load_dotenv()
ProviningSystems = {
    'huawei': os.environ.get('PROVSYS_H'),
    'datacom': os.environ.get('PROVSYS_D'),
    'anm': os.environ.get('PROVSYS_A'),
    'epon': os.environ.get('PROVSYS_E')
}

current_date = date.today()

current_day = current_date.strftime('%d')
current_month = current_date.strftime('%m')
tomorrow_date = current_date + datetime.timedelta(days=1)

tomorrow_day = tomorrow_date.strftime('%d')
tomorrow_month = tomorrow_date.strftime('%m')

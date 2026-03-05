import os
import json

class Menu:
    def __init__(self, dominio):
        if not (os.path.isdir('scans')):
            os.mkdir('scans')
        if not (os.path.isdir(f'scans/{dominio}')):
            os.mkdir(f'scans/{dominio}')

    def menu():
        while True:
            pastas = os.listdir('scans/')
            id = 0
            for pasta in pastas:
                print(f'{id}. {pasta}')
                id += 1
            print('\nSelecione o ID ou exit para sair:')
            try:
                select = input('[ID] >')
                if select.lower() == 'exit' or select.lower() == 'sair':
                    exit(0)
                else:
                    select = int(select)
            except ValueError:
                print('Input inválido.\n')
                continue

            if select >= len(pastas) or select < 0:
                print('ID inválido.\n')
            else:

                pasta = pastas[select]

                with open(f'scans/{pasta}/{pasta}.whois', 'r') as f:
                    whois = f.read()
                    f.close()
                
                with open(f'scans/{pasta}/{pasta}-subdomains.json', 'r') as f:
                    subdominios = json.loads(f.read())
                    ipv4 = subdominios['ipv4']
                    ipv6 = subdominios['ipv6']
                    f.close()

                with open(f'scans/{pasta}/{pasta}-cname.json', 'r') as f:
                    cnames = json.loads(f.read())
                    f.close()
                
                print('\nListando registros...\n')
                print(f'Subdominios IPv4:   {len(ipv4)}')
                print(f'Subdominios IPv6:   {len(ipv6)}')
                print(f'Cnames encontrados: {len(cnames)}')
                if whois:
                    print(f'Whois disponível:   Sim')
                else:
                    print(f'Whois disponível:   Não')
                print('\n')

                while True:
                    print('Opções:\nlist ipv4 -> Listar subdominios IPv4\nlist ipv6 -> Listar subdominios IPv6\nlist sub -> Listar todos os domínios (IPv4 e IPv6)\nlist cnames -> Listar CNAMES\nwhois -> Mostrar whois (se houver)\nlist all -> Listar tudo\nback -> Para voltar\nexit -> para sair\n')
                    select = input('> ')
                    print('\n')
                    if select == 'list ipv4':
                        for ip in ipv4:
                            print(f'{ip} -> {ipv4[ip]}')

                    elif select == 'list ipv6':
                        for ip in ipv6:
                            print(f'{ip} -> {ipv6[ip]}')
                    
                    elif select == 'list sub':
                        print('Subdominios IPv4:')
                        for ip in ipv4:
                            print(f'{ip} -> {ipv4[ip]}')
                        print('\n')
                        print('Subdominios IPv6:')
                        for ip in ipv6:
                            print(f'{ip} -> {ipv6[ip]}')
                    elif select == 'list cnames' or select == 'list cname':
                        for dominio in cnames:
                            print(f'{dominio} é um alias para {cnames[dominio]}')
                    elif select == 'whois' or select == 'list whois':
                        if whois:
                            print(whois)
                        else:
                            print('Não há arquivo whois deste domínio.')
                    elif select == 'list all' or select == 'all':
                        print('Subdominios IPv4:')
                        for ip in ipv4:
                            print(f'{ip} -> {ipv4[ip]}')
                        print('\n')
                        print('Subdominios IPv6:')
                        for ip in ipv6:
                            print(f'{ip} -> {ipv6[ip]}')
                        print('\n')
                        print('CNAMES:')
                        for dominio in cnames:
                            print(f'{dominio} é um alias para {cnames[dominio]}')
                        print('\n')
                        print('WHOIS:')
                        print(whois)
                    elif select.lower() == 'back':
                        break
                    elif select.lower() == 'exit':
                        exit(0)
                    else:
                        print('Comando inválido.')
                    print('\n')
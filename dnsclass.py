import socket
import dns.resolver
import time
import json

class DNSscan:
    def subdomainBruteForce(dominio, wordlist):
        def DNSipv4(dominio):
            try:
                dados = socket.getaddrinfo(dominio, None, socket.AF_INET)
                addr = dados[2][4][0]
                print(f"{dominio}: {addr}")
                return addr
            except  socket.gaierror:
                return 0

        def DNSipv6(dominio):
            try:
                dados = socket.getaddrinfo(dominio, None, socket.AF_INET6)
                addr = dados[2][4][0]
                print(f"{dominio}: {addr}")
                return addr
            except  socket.gaierror:
                return 0

        consultado = []
        dominios4 = {}
        dominios6 = {}
        dominios = {}

        with open(wordlist) as wordlist:
            for i in wordlist.readlines():
                i = i.replace('\n', '')
                dominio_montado = f"{i}.{dominio}"

                if dominio_montado not in consultado:
                    addr4 = DNSipv4(dominio_montado)
                    addr6 = DNSipv6(dominio_montado)

                    if addr4 != 0:
                        dominios4[dominio_montado] = addr4
                    if addr6 != 0:
                        dominios6[dominio_montado] = addr6
                    consultado.append(dominio_montado)

        dominios["ipv4"] = dominios4
        dominios["ipv6"] = dominios6

        dominios_json = json.dumps(dominios)

        with open(f"{dominio}-subdomains.json", 'w') as f:
            f.write(dominios_json)
            f.close()
        print(f'Arquivo JSON "{dominio}-subdomains.json" criado.')
        
    def cnameCheck(dominio, wordlist):
        cnames = {}
        with open(wordlist) as wordlist:
            for i in wordlist.readlines():
                i = i.replace('\n', '')
                subdominio = f'{i}.{dominio}'
                while True:
                    try:
                        resposta = dns.resolver.resolve(subdominio, "CNAME")
                        cname = resposta[0].target
                        cnames[subdominio] = str(cname)
                        print(f'{subdominio} tem um alias {cname}')
                        break
                    except dns.resolver.NoAnswer:
                        break
                    except dns.resolver.NXDOMAIN:
                        break
                    except dns.resolver.NoNameservers:
                        break
                    except dns.resolver.LifetimeTimeout:
                        time.sleep(2)

        cnames_json = json.dumps(cnames)

        with open(f'{dominio}-cname.json', 'w') as f:
            f.write(cnames_json)
            f.close()
        print(f'Arquivo JSON "{dominio}-cname.json" criado.')

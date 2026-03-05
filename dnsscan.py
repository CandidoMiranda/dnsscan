import dnsclass
import sys
import dnsmenu

inicio = dnsmenu.Menu

if len(sys.argv) < 2:
    inicio.menu()
else:
    dominio = sys.argv[1]
    wordlist = sys.argv[2]

    inicio(dominio)

    dns = dnsclass.DNSscan

    print('\n')
    print(f'*** Consultando WHOIS - {dominio} ***\n')
    dns.whois(dominio)
    print('-------------------------------------\n\n')

    print(f'*** Listando subdomínios - {dominio} ***\n')
    dns.subdomainBruteForce(dominio, wordlist)
    print('-------------------------------------\n\n')

    print(f'*** Listando CNAMEs - {dominio} ***\n')
    dns.cnameCheck(dominio, wordlist)
    print('-------------------------------------\n\n')

    inicio.menu()
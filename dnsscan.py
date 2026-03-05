import dnsclass
import sys

dominio = sys.argv[1]
wordlist = sys.argv[2]

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

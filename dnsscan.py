import dnsclass
import sys

dominio = sys.argv[1]
wordlist = sys.argv[2]

dns = dnsclass.DNSscan
#dns.subdomainBruteForce(dominio, wordlist)
dns.cnameCheck(dominio, wordlist)
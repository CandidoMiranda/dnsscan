import socket
import sys
import json

def openSocket(whois, dominio):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((whois,43))
    s.send(dominio.encode())
    return s

dominio = sys.argv[1]
dominio = dominio + '\r\n'

s = openSocket('whois.iana.org', dominio)
whois = s.recv(1024).decode().split('refer:        ')[1].split('\n')[0]
s.close()

s = openSocket(whois, dominio)
whois = s.recv(1024).decode().split(' Registrar WHOIS Server: ')[1].split('\r')[0]
s.close()

s = openSocket(whois, dominio)

resposta = ''
while True:
    data = s.recv(8192)
    if data:
        resposta += data.decode()
    else:
        break
s.close()

dominio = dominio.replace('\r\n','')

with open(f'{dominio}.whois', 'w') as f:
    f.write(resposta)
    f.close()

print(resposta)

'''
Crie um código em Python que teste se o site Pudim está acessivel pelo
computador usado.
'''

import requests
import urllib.request

url = "https://pudim.com.br/"


try:
    response = requests.get(url, timeout=5)
    if response.status_code == 200:
        print(f"\033[33mConsegui acessar o site Pudim com sucesso. Cod: {response.status_code}\033[m")
    else:
        print(f"\033[31mO site Pudim não está acessível no momento. Erro: {response.status_code}\033[m")
except:
    print("Não foi possivel acessar. Tente novamente.")



site = "https://www.jw.org/pt/"

try:
    retorno = urllib.request.urlopen(site)
except urllib.error.URLError:
    print(f"\033[31mO site JW não está acessível no momento.\033[m")  
else:
    print(f"\033[33mConsegui acessar o site JW com sucesso.\033[m")
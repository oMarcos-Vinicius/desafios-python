'''
Faça um programa que leia o ano qualquer e mostre se ele é BISSEXTO
'''
from datetime import date

ano = int(input("Que ano quer analisar? Coloque 0 para analisar o ano atual: "))

if ano == 0:
    ano = date.today().year

if (ano % 4 == 0):
    if (ano % 100 == 0):
        if (ano % 400 == 0):
            print(f"O ano {ano} é BISSEXTO")
        else:
            print(f"O ano {ano} não é BISSEXTO")
    else:
        print(f"O ano {ano} é BISSEXTO")
else:
    print(f"O ano {ano} não é BISSEXTO")

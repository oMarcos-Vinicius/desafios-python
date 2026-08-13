'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear
6 números entre 1 a 60 para cada jogo, cadastrando tudo em uma lista
composta.
'''

from random import randint
from time import sleep

print("-"*30)
print("{:^30}".format("JOGO DA MEGA SENA"))
print("-"*30)

quant = int(input("Quantos jogos você quer que eu sorteie? "))
print(f"-=-=-= SORTEARNDO {quant} {"JOGO" if quant == 1 else "JOGOS"} -=-=-=")

jogo = list()
numeros = list()

for c in range(1, (quant+1)):
    numeros.clear()
    i = 0
    while i < 6:
        valor = randint(0,60)
        if valor not in numeros:
            numeros.append(valor)
            i += 1
    numeros.sort()
    jogo.append(numeros[:])

for pos, jogadas in enumerate(jogo):
    sleep(1.5)
    print(f"Jogo {pos+1}: {jogadas}")

print(f"-=-=-= < BOA SORTE! > -=-=-=")

#print(f"Todos os jogos: {jogo}")
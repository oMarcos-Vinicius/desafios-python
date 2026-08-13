'''
Crie um programa que faça o computador jogar JoKenPô com você
'''
from random import randint
from time import sleep

print('''
Suas opções
[0] PEDRA
[1] PAPEL
[2] TESOURA
''')

option_jogador = int(input("Qual é a sua jogada? "))
option_computador = randint(0,2)

if option_jogador == 0:
    jogador = "PEDRA"
elif option_jogador == 1:
    jogador = "PAPEL"
else:
    jogador = "TESOURA"

if option_computador == 0:
    computador = "PEDRA"
elif option_computador == 1:
    computador = "PAPEL"
else:
    computador = "TESOURA"


sleep(0.2)
print("JO")
sleep(0.5)
print("KEN")
sleep(0.5)
print("PO!!!")
sleep(0.2)


print("-=" * 20)
print(f"Computador jogou {computador}")
print(f"Jogador jogou {jogador}")
print("-=" * 20)

if (option_jogador == 0) and (option_computador == 2):
    vencedor = "JOGADOR VENCE"
elif (option_jogador == 1) and (option_computador == 0):
    vencedor = "JOGADOR VENCE"
elif (option_jogador == 2) and (option_computador == 1):
    vencedor = "JOGADOR VENCE"
elif (option_jogador == 0) and (option_computador == 1):
    vencedor = "COMPUTADOR VENCE"
elif (option_jogador == 1) and (option_computador == 2):
    vencedor = "COMPUTADOR VENCE"
elif (option_jogador == 2) and (option_computador == 0):
    vencedor = "COMPUTADOR VENCE"
elif option_jogador == option_computador:
    vencedor = "FOI UM EMPATE"

print(vencedor)

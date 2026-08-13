'''
Faça um programa que tenha uma função chamada ficha(), que receba dois parametros
opcionais: o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogagor, mesmo que algum dado não
tenha sido informado corretamente.
'''

def ficha(jogador="", gols=""):
    if gols.strip() == "":
        gols = 0
    else:
        int(gols)

    if jogador.strip() == "":
        jogador = "<desconhecido>"

    print(f"O jogador {jogador} fez {gols} gol(s) no campeonato")

print("-" * 30)
jogador = str(input("Nome do jogador: "))
gols = str(input("Número de gols: "))

ficha(jogador, gols)
ficha()
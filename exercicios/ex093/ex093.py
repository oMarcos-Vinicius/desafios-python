'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa
vai ler o nome do jogador e quantas partidas jogou. Depois vai ler a quantidade de gols
feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo
o total de gols feitos durante o campeonato.
'''

jogador = {}
jogador['nome'] = str(input("Nome do jogador: "))
partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
jogador['gols'] = list()

for c in range(1, partidas+1):
    jogador['gols'].append(int(input(f"Quantos gol na partida {c}? ")))

jogador['total'] = sum(jogador['gols'])
print("-="*30)
print(jogador)
print("-="*30)
for key, value in jogador.items():
    print(f"O campo {key} tem o valor {value}.")
print("-="*30)
print(f"O jogador {jogador['nome']} jogou {partidas} partidas.")

for pos, valor in enumerate(jogador['gols']):
    print(f"    => Na partida {pos+1}, fez {valor} {"gols" if valor != 1 else "gol"}.")
print(f"Foi um total de {jogador['total']} gols")
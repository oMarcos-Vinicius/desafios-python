'''
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário. No final, coloque esse dicionario em ordem,
sabendo que o vencedor tirou o maior número no dado.
'''

from random import randint
from time import sleep
from operator import itemgetter

dados = {}

print("-="*30)
print("== Jogando os dados ==")
for c in range(1,5):
    dados[f'jogador{c}'] = randint(1,6)
    sleep(1)
    print(f"O jogador{c} tirou {dados[f'jogador{c}']}")

ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)

print("-="*30)
print("== Ranking dos jogadores ==")
for jogada, jogador in enumerate(ranking):
    sleep(1)
    print(f"    {jogada+1}º lugar: {jogador[0]} com {jogador[1]}")

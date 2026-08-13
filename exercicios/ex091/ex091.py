'''
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário. No final, coloque esse dicionario em ordem,
sabendo que o vencedor tirou o maior número no dado.
'''

from random import randint
from time import sleep

dados = {}

for c in range(1,5):
    dados[f'jogador{c}'] = randint(1,6)
    sleep(1)
    print(f"O jogador{c} tirou {dados[f'jogador{c}']}")

dados_ordenados = []
for valor in dados.values():
    dados_ordenados.append(valor)
dados_ordenados.sort(reverse="True")

dados_copia = dados.copy()
dados.clear()

for valor in dados_ordenados:
    for jogador, jogada in dados_copia.items():
        if valor == jogada:
            dados[jogador] = jogada
            del dados_copia[jogador]
            break

print("Ranking dos jogadores:")
c = 1
for jogador, jogada in dados.items():
    print(f"{c}º lugar: {jogador} com {jogada}")
    c += 1
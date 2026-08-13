'''
Aprimore o Desafio 093 para que ele funcione com vários jogadores, incluindo um 
sistema de visualização de detalhes do aproveitamemento de cada jogador.
'''

jogadores = list()
jogador = {}

while True:
    print("-"*40)
    jogador['nome'] = str(input("Nome do jogador: "))
    partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    jogador['gols'] = list()

    for c in range(1, partidas+1):
        jogador['gols'].append(int(input(f"Quantos gol na partida {c}? ")))

    jogador['total'] = sum(jogador['gols'])

    jogadores.append(jogador.copy())

    resp = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if resp in "N":
        break

    jogador.clear()

print("-="*30)

print(f"{"cod":<4}{"nome":<15}{"gols":<15}{"total":<5}")
print("-"*40)

for pos, jogador in enumerate(jogadores):
    print(f"{pos:3}", end=" ")
    for valor in jogador.values():
         print(f"{str(valor):<15}",end="")
    print()

while True:
    print("-"*40)
    player = int(input("Mostre dados de qual jogador? "))

    if (player >= 0) and (player <= len(jogadores)-1):
        print(f"-- LEVANTAMENTO DO JOGADOR {jogadores[player]['nome']}")
        for pos, valor in enumerate(jogadores[player]['gols']):
            print(f"    => Na partida {pos+1}, fez {valor} {"gols" if valor != 1 else "gol"}.")
    elif player == 999:
        break
    else:
        print(f"ERRO! Não existe jogador com o códido {player}")
print("<< VOLTE SEMPRE >>")
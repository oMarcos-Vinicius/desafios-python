'''
Faça um programa que jogue par ou impar com o computador. O jogo
só será interrompido quando o jogador PERDER, mostrando o total
de vitórias consecutivas que ele conquistou no final do jogo.
'''
from random import randint

print("-="*20)
print("VAMOS JOGAR PAR OU ÍMPAR")
print("-="*20)
vitorias = 0

while True:

    pc = randint(0,10)
    valor = int(input("Digite um valor: "))
    soma = pc + valor
    resultado = "DEU PAR" if soma % 2 == 0 else "DEU IMPAR"
    escolha = " "
    
    while escolha not in "PI":
        escolha = str(input("Par ou Ímpar? [P/I] ")).strip().upper()[0]

    print(escolha)
    print("-"*40)
    print(f"Você jogou {valor} e o computador jogou {pc}. Total de {soma} {resultado}")
    print("-"*40)

    if escolha in "Pp":
        if resultado == "DEU IMPAR":
            print("Você perdeu")
            break
    elif escolha in "Ii":
        if resultado == "DEU PAR":
            print("Você perdeu")
            break
    
    vitorias += 1
    print("Você venceu!")
    print("Vamos jogar novamente...")
    print("-="*20)

print(f"GAME OVER! Você venceu {vitorias} vezes.")






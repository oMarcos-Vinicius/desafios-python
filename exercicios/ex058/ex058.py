'''
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em
um número entre 0 e 10. Só que agora o jogador vai tentar 
adivinhar até acertar, mostrando no final quantos palpites foram
necessários para vencer.
'''

from random import randint

num_sorteado = randint(0,10)
num_tentado = 11
tentativas = 0

print("Sou seu computador...")
print("Acabei de pensar em um número entre 0 a 10.")
print("Será que você consegue adivinhar qual foi?")

while num_tentado != num_sorteado:
    num_tentado = int(input("Qual é o seu palpite? "))
    if num_tentado < num_sorteado:
        print("Mais... Tente mais um vez")
    elif num_tentado > num_sorteado:
        print("Menos... Tente mais um vez")
    tentativas += 1
print(f"Acertou na {tentativas}ª tentativa. Parabéns!")

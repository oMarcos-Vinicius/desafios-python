from random import randint
from time import sleep

print("-=-"*30)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print("-=-"*30)

num_sorteado = randint(0, 5)

num_escolhido = int(input("Em que numero eu pensei? "))

print("PROCESSANDO...")
sleep(2)

if num_escolhido == num_sorteado:
    print("PARABÉNS! Você conseguiu me vencer!")
else:
    print(f"GANHEI! Eu pensei no número {num_sorteado} e não no {num_escolhido}!")


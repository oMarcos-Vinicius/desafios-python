'''
Crie um programa que vai gerar cinco números aleatórios e colocar
em uma tupla. Depois disso, mostre a listagem de números gerados
e também indique o menor e o maior valor qe estão na tupla.
'''

from random import randint

sorteado = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print("Os valores sorteados foram: ",end="")

for pos, num in enumerate(sorteado):
    print(f"{num}",end=" ")
    if pos == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

print(f"\nO maior valor sorteado foi {maior}")
print(f"O maior valor sorteado foi {max(sorteado)}") # Posso usar o metodo max()
print(f"O menor valor sorteado foi {menor}")
print(f"O menor valor sorteado foi {min(sorteado)}") # Posso usar o metodo min()
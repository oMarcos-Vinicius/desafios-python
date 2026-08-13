'''
Faça um programa que tenha uma lista chamada números e duas funções chamadas
sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los
dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES
sorteados pela função anterior.
'''

from random import randint
from time import sleep

def somaPar(numeros):
    soma = 0
    for num in numeros:
        if num % 2 == 0:
            soma += num
    print(f"Somando os valores pares de {numeros}, temos {soma}")

def sorteia(numeros):
    print("Sorteando os valores da lista: ", end="", flush=True)
    for c in range(0,5):
        num_sorteado = randint(1,10)
        sleep(0.5)
        print(num_sorteado, end=" ", flush=True)
        numeros.append(num_sorteado)
    print("PRONTO!")

numeros = list()
sorteia(numeros)
somaPar(numeros)

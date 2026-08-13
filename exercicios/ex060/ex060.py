'''
Faça um programa que leia um número qualquer e mostre
seu fatorial. EX: 5! = 5x4x3x2x1 = 120
'''

valor = int(input("Digite um valor para \ncalcular seu fatorial: "))
valor_for = valor
contador = valor - 1

#Usando while

print(f"Calculando {valor}! = {valor}", end="")

while contador > 0:
    print(f" x {contador}", end="")
    valor = valor * contador
    contador -= 1
print(f" = {valor}")

#Usando for

print(f"Calculando {valor_for}! = {valor_for}", end="")

for c in range((valor_for-1), 0, -1):
    print(f" x {c}", end="")
    valor_for = valor_for * c

print(f" = {valor_for}")
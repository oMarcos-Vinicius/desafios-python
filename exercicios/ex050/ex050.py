'''
Desenvolva um programa que leia seis números interios e mostre a soma 
apenas daquele sque forem pares. se o valor digitado for impar,
desconsidere-o
'''
soma = 0
contador = 0

for c in range(0,6):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        contador += 1
        soma += numero
print(f"Você informou {contador} números pares e a soma foi {soma}")

    
'''
Crie um programa onde o usuário possa digitar vários valores numéricos
e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não
será adicionado. No final, serão exibidos todos os valores únicos
digitados, em ordem crescente. 
'''

numeros = []

while True:
    valor = int(input("Digite um valor: "))

    if valor not in numeros:
        numeros.append(valor)
        print("Valor adicionado com sucesso...")
    else:
        print("Valor duplicado! Não vou adicionar...")

    parar = str(input("Quer continuar? [S/N] ")).upper().strip()

    if parar in "N":
        break
print("-"*30)
numeros.sort()
print(f"Você digitou os valores {numeros}")

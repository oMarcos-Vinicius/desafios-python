'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão contar apenas os valores
pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
'''

lista_completa = []
lista_pares = []
lista_impares = []

while True:
    lista_completa.append(int(input("Digite um número: ")))

    resposta = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if resposta in "Nn":
        break

for numero in lista_completa:
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)

print("A lista completa é", lista_completa)
print("A lista de pares é", lista_pares)
print("A lista de ímpares é", lista_impares)
'''
Crie um programa que ailer vários números e colocar em uma lista.
Depois disso, moste:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valore 5 foi digitado e está ou não na lista.
'''

numeros = []

while True:
    numeros.append(int(input("Digite um valor: ")))
    resposta = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if resposta in "Nn":
        break

numeros.sort(reverse=True)
print("-="*30)
print(f"Você digitou {len(numeros)} elementos.")
print("Os valores em ordem decrescente são:", numeros)
if 5 in numeros:
    print(f"O valor 5 faz parte da sua lista e está na posição {numeros.index(5)}")
else:
    print("O valor 5 não foi encontrado na suas lista!")


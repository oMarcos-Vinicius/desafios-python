'''
Faça um programa que leia o peso de cinco pessoas. No final,
mostre qual foi o maior e o menos peso lidos
'''
leve = 0
pesado = 0

for i in range(1,6):
    peso = float(input(f"Peso da {i}ª pessoa: Kg "))
    if i == 1:
        pesado = peso
        leve = peso
    else:
        if peso > pesado:
            pesado = peso
        if peso < leve:
            leve = peso

print(f"O maior peso lido foi de {pesado}Kg")
print(f"O menor peso lido foi de {leve}Kg")
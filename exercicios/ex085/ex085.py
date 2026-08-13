'''
Crie um programa onde o usuário possa digitar sete valores numéricos
e cadastra-os em uma lista única que mantenha separados os valores
pares e ímpares. No final, mostre os valores pares e ímpares em
ordem crescente.
'''

valores = [[],[]]

for c in range(1,8):
    valor = int(input(f"Digite o {c}º valor: "))
    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)

valores[0].sort()
valores[1].sort()

print("Os valores pares digitados foram:", valores[0])
print("Os valores ímpares digitados foram:", valores[1])
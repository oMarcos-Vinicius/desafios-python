'''
Crei um programa que simule o funcionamento de um caixa 
eletrônico. No início, pergunte ao usuário qual sreá o valor
a ser sacado (número inteiro) e o programa vai informar 
quantas cédulas de cada valor serão entregues.

Obs.: Considere que o caixa possui cédulas de R$50, R$20 
R$10 e R$1
'''

print("="*40)
print("{:^40}".format("Banco CEV"))
print("="*40)
valor = int(input("Qual valor você quer sacar? R$"))

cedula50 = cedula20 = cedula10 = cedula1 = 0
cedulas = [50, 20, 10, 1]

c = 0
while True:

    if c == 0:
        cedula50 = valor // cedulas[c]
        if cedula50 != 0: print(f"valor de {cedula50} cédulas de R$50")
    elif c == 1:
        cedula20 = valor // cedulas[c]
        if cedula20 != 0: print(f"valor de {cedula20} cédulas de R$20")
    elif c == 2:
        cedula10 = valor // cedulas[c]
        if cedula10 != 0: print(f"valor de {cedula10} cédulas de R$10")
    else:
        cedula1 = valor // cedulas[c]
        if cedula1 != 0: print(f"valor de {cedula1} cédulas de R$1")

    valor -= (cedulas[c] * (valor // cedulas[c]))

    if valor == 0:
        break 
    c += 1

print("="*40)
print("Volte sempre ao Banco CEV! Tenha um bom dia!")
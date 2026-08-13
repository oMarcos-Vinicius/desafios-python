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
total_cedulas = 0
cedula = 50

while True:
    while valor >= cedula:
        valor -= cedula
        total_cedulas += 1
    print(f"Total de {total_cedulas} cédulas de R${cedula}")
    total_cedulas = 0
    
    if valor == 0:
        break
    elif valor < 10:
        cedula = 1
    elif valor < 20:
        cedula = 10
    elif valor < 50:
        cedula = 20

print("="*40)
print("Volte sempre ao Banco CEV! Tenha um bom dia!")
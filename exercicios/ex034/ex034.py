'''
Escreva um programa que pergunta o salário de um funcionário e calcule o valor do seu aumento.
para salários superiores a R$1.250, calcule um aumento de 10%
Para os inferiores ou iguais, o aumento é de 15%
'''

salario = float(input("Qual é o salario do funcionário? R$"))
novo_salario = 0

if salario >= 1250:
    novo_salario = salario + (salario * 0.10)
else:
    novo_salario = salario + (salario * 0.15)

print(f"Quem ganhava R${salario:.2f} passsa a ganhar R${novo_salario:.2f}")
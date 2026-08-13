'''
Escreva um programa que leia a velicidade de um carro.
Se ele ultrapassar 80Km/hm, mostre uma mensagem dizendo que ele foi multado
A multa vai custar R$7,00 por cada Km acima do limite
'''

from termcolor import colored

velocidade = int(input("Qual é a velocidade atual do carro? "))

if velocidade > 80:
    print(colored("MULTADO! Você excedeu o limite permitido que é de 80Km/h", "red"))
    print(colored(f"Você deve pagar uma multa de R${((velocidade-80)*7):.2f}", "red", attrs=["bold"]))

print(colored("Tenha um bom dia! Dirija com segurança!", "yellow"))
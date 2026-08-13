'''
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR
'''
from termcolor import colored

number = (int(input("Me diga um número qualquer: ")))

if number % 2 == 0:
    print(f"O número {number} é", colored("PAR", "blue"))
else:
    print(f"O número {number} é", colored("ÍMPAR", "blue"))
    
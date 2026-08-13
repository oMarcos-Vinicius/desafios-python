'''
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainsa não atingiram a maioridade
e quantas já são maiores
'''
from datetime import date

maiores = 0
menores = 0

ano_atual = date.today().year

for i in range(1,8):
    ano = int(input(f"Em que ano a {i}º pessoa nasceu? "))
    if (ano_atual - ano) >= 18:
        maiores += 1
    else:
        menores += 1

print(f"Ao todo tivemos {maiores} pessoas maiores de idade")
print(f"E também tivemos {menores} pessoas maiores de idade")
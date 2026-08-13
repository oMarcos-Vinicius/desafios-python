'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar
- Se é a hora de se alistar
- Se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
'''
from datetime import date

nascimento = int(input("Ano de nascimento: "))
ano_atual = date.today().year
idade = ano_atual - nascimento

print(f"Quem nasceu em {nascimento} tem {idade} anos em {ano_atual}")

if idade < 18:
    print(f"Ainda faltam {18 - idade} anos para o alistamento")
    print(f"Seu alistamanto será {nascimento + 18}")
elif idade > 18:
    print(f"Você já deveria ter se alistado há {ano_atual - (nascimento + 18)} anos")
    print(f"Seu alistamento foi em {nascimento + 18}")
else:
    print("Você tem que se alistar IMEDIATAMENTE!")

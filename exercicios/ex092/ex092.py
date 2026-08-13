'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e
cadastre-os (com idade) em um dicionário, se por acaso a CTPS for diferente de
Zero, o dicionário receberá também o ano de contratação e o salario. Calcule e 
acrescente, além da idade, com quantos anos a pessoa vai se aposentar
'''
from datetime import datetime

funcionario = dict()

funcionario['nome'] = str(input("Nome: "))
nascimento = int(input("Ano de nascimento: "))
funcionario['idade'] = (datetime.now().year) - nascimento
funcionario['ctps'] = str(input("Carteira de Trabalho (0 caso não tenha): "))

if funcionario['ctps'] != 0:
    funcionario['contratacao'] = int(input("Ano de contratação: "))
    funcionario['salario'] = float(input("Salário: R$"))
    funcionario['aposentadoria'] = (funcionario['contratacao'] - nascimento) + 35
print("-="*30)
for chave, valor in funcionario.items():
    print(f"{chave} tem o valor de {valor}")


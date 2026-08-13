'''
Faça um programa que leia nome e média de um aluno, guardando também
a situação em um dicionário. No final, mostre o conteúdo da estrutura
na tela.
'''

alunos = dict()

alunos['Nome'] = str(input("Nome: "))
alunos['Média'] = float(input(f"Média de {alunos['Nome']}: "))

if alunos['Média'] >= 7:
    alunos['Situação'] = "Aprovado"
elif (alunos['Média'] > 5) and (alunos['Média'] < 7):
    alunos['Situação'] = "Recuperação"
else:
    alunos['Situação'] = "Reprovado"
print("-="*30)

for chave, valor in alunos.items():
    print(f" - {chave} é igual a {valor}")

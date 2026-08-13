'''
Crie um programa que leia nome, sexo, e idade de várias pessoas, guardando os dados
de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
a) Quantas pessoas foram cadastradas
b) A média de idade do grupo
c) Uma lista com toas as mulheres
d) Uma lista com todoas as pessoas com idade acima da média.
'''

pessoas = list()
pessoa = dict()

while True:

    pessoa['nome'] = str(input("Nome: "))
    pessoa['sexo'] = str(input("Sexo: [M/F] ")).upper().strip()[0]
    pessoa['idade'] = int(input("Idade: "))

    pessoas.append(pessoa.copy())
    pessoa.clear()

    resp = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if resp in "N":
        break
print("-=" * 30)
print(f" - O grupo tem {len(pessoas)} pessoas.")
soma = 0
for pessoa in pessoas:
    soma += pessoa['idade']
media = soma / len(pessoas)
print(f" - A média de idade é de {media:.0f} anos.")
print(f" - As mulheres cadastradas fora: ", end="")
for pessoa in pessoas:
    if pessoa['sexo'] in "F":
        print(pessoa['nome'], end=" ")
print(f"\n - Lista das pessoas que estão acima da média: ")
print()
for pessoa in pessoas:
    if pessoa['idade'] >= media:
        print(f"nome = {pessoa['nome']}; sexo = {pessoa['sexo']}, idade = {pessoa['idade']};")
        print()
print("<< ENCERRANDO >>")
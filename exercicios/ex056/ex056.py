'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre:
- A média de idade do grupo
- Qual é o nome do homem mais velho
- Quantas mulheres têm menos de 20 anos
'''
idades = 0
media = 0
homem_velho = ""
idade_velho = 0
idade_mulheres = 0

for c in range(1,5):
    print(f"----- {c}ª PESSOA -----")
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip().upper()

    idades += idade

    if sexo == "M":
        if idade > idade_velho:
            homem_velho = nome
            idade_velho = idade
    else:
        if idade <= 20:
            idade_mulheres += 1

print(f"A média de idade do grupo é de {(idades/4):.1f} anos")
print(f"O homem mais velho tem {idade_velho} anos e se chama {homem_velho}.")
print(f"Ao todo são {idade_mulheres} mulheres com menos de 20 anos")
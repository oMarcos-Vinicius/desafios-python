'''
Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá pergntar se o 
usuário quer ou não continuar. No final, mostre:
a - Quantas pessoas tem mais de 18 anos
b - Quantos homens foram cadastrados.
c - Quantas mulheres tem menos de 20 anos.
'''
a = 0
b = 0
c = 0

while True:
    print("-"*30)
    print("   CADASTRE UMA PESSOA   ")
    print("-"*30)

    sexo = " "
    continuar = " "

    idade = int(input("Idade: "))

    while sexo not in "MF":
        sexo = str(input("Sexo: [M/F] ")).strip().upper()[0]

    if idade >= 18:
        a += 1

    if sexo in "M":
        b += 1
    elif sexo in "F":
        if idade >= 20:
            c += 1
    
    while continuar not in "SN":
        continuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]

    if continuar == "N":
        break

print("====== FIM DO PROGRAMA ======")
print(f"a - O total de pessoas com mais de 18 anos: {a}")
print(f"b - Ao todo temos {b} homens cadastrados")
print(f"c - E temos {c} mulheres com menos de 20 anos")
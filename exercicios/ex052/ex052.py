'''
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo
'''
numero = int(input("Digite um número: "))
vezes = 0

for c in range(1, numero+1):
    if numero % c == 0:
        print(f"\033[33m",c,end="")
        vezes += 1
    else:
        print(f"\033[31m",c,end="")
print(f"\n \033[mO numero {numero} foi divisível {vezes} vezes")
if vezes == 2:
    print("E por isso ele É PRIMO")
else:
    print("E por isso ele NÃO É PRIMO")
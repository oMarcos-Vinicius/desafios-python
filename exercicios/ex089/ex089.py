'''
Crie um programa que leia nome e duas notas de vários alunos e
guarde tudo em uma lista composta. No final, mostre um boletim
contendo a média de cada um e permita que o usuário possa
mostrar as notas de cada aluno individualmente.
'''

boletim = list()


while True:

    aluno = str(input("Nome: "))
    nota1 = float(input(f"Nota 1: "))
    nota2 = float(input(f"Nota 2: "))
    boletim.append([aluno, [nota1, nota2]])

    resp = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]
    if resp in "N":
        break

print("-="*20)
print(f"{"No.":<4}{"NOME":<20}{"MÉDIA":10}")
print("-"*34)

for aluno in range(0,len(boletim)):
    print(f"{aluno:<4}{boletim[aluno][0]:20}", end="")
    soma = 0
    soma += boletim[aluno][1][0] + boletim[aluno][1][1]
    print(f"{soma/2:.1f}")

print("-"*34)

while True:

    resp = int(input("Mostrar notas de qual aluno? (999 interromper) "))

    if resp == 999:
        break

    if resp < len(boletim):
        print(f"Notas do(a) {boletim[resp][0]} são: {boletim[resp][1]}")
    else:
        print("Aluno não encontrado. Tente novamente!")
    print("-"*34)
    
print("FINALIZANDO...")
print("<<< VOLTE SEMPRE >>>")
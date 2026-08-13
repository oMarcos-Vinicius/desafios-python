#Embaralhar um lista

from random import shuffle

alunos = []

alunos.append(str(input("Primeiro aluno: ")))
alunos.append(str(input("Segundo aluno: ")))
alunos.append(str(input("Terceiro aluno: ")))
alunos.append(str(input("Quarto aluno: ")))

shuffle(alunos)

print(f"A ordem de apresentação será: {alunos}")

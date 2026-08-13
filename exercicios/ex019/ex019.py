#Sortear uma pessoa

import random

alunos = []

alunos.append(str(input("Primeiro aluno: ")))
alunos.append(str(input("Segundo aluno: ")))
alunos.append(str(input("Terceiro aluno: ")))
alunos.append(str(input("Quanto aluno: ")))

aluno_sorteado = random.choice(alunos)

print("O aluno escolhido foi",aluno_sorteado)
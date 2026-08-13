'''
Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERÇÃO
- Média 7.0 ou superior: APROVADO 
'''
nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))

media = (nota1 + nota2) / 2

print(f"Tirando {nota1:.1f} e {nota2:.1f}, a média do aluno é {media:.1f}")

if media >= 7.0:
    print("O aluno está \033[4;32;40mAPROVADO\033[m")
elif (media >= 5) and (media < 7):
    print("O aluno está em \033[4;33;40mRECUPERAÇÃO\033[m")
else:
    print("O aluno está \033[4;31;40mREPROVADO\033[m")

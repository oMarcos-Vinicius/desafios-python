'''
Refaça o DESAFIO 09, mostrando a tabuada de um número 
que o usuário escolher, só que agora utilizando um laço for
'''
numero = int(input("Digite um numero para saber sua tabuada do 10: "))

print("--------------")

for c in range(1,11):
    print(f"{numero} x {c:2} = {numero*c}")

print("--------------")

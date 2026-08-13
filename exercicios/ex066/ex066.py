'''
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai para quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos números 
foram digitados e qual foi a soma entre eles (desconsiderando
o flag)
'''
contagem = soma = numero = 0

while True:
    numero = int(input("Digite um número [999 para sair]: "))
    if numero == 999:
        break   
    soma += numero
    contagem += 1

print(f"Você digitou {contagem} numeros e a soma entre eles foi de {soma}.")
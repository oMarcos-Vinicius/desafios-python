'''
Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e 
qual foi o maior e menor valores lidos. O programa deve perguntar
ao usuário se ele quer ou não continuar a digitar valores.
'''
quantidade = soma = maior = menor = 0
continuar = "S"

while continuar not in 'Nn':
    numero = int(input("Digite um número: "))
    quantidade += 1
    soma += numero
    if quantidade == 1:
        maior = menor = numero
    else:    
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    continuar = str(input("Quer continuar: [S/N] ")).strip().upper()[0]

print(f"Você digitou {quantidade} números e a média foi de {soma/quantidade:.2f}")
print(f"O maior valor foi {maior} e o menos foi {menor}")
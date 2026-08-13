'''
Faça um programa que leia três números e mostre qual é o maior e qual é o menor
'''

n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
n3 = int(input("Terceiro valor: "))

if n1 > n2:
    if n1 > n3:
        maior = n1
        if n2 > n3:
            menor = n3
        else:
            menor = n2
    else:
        maior = n3
        menor = n2
else:
    if n2 > n3:
        maior = n2
        if n1 > n3:
            menor = n3
        else:
            menor = n1
    else:
        maior = n3
        menor = n1

print(f"O menor valor digitado foi {menor}")
print(f"O maior valor digitado foi {maior}")

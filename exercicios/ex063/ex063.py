'''
Escreva um programa que leia um número n inteiro qualquer e mostre
na tela os n primeiros elementos de uma Sequência de Fibonacci
'''

print("-"*30)
print("Sequência de Fibonacci")
print("-"*30)

termos = int(input("Quantos termos você quer mostrar? "))
print("~"*30)

resultado = 0
termo_atual = 0
termo_anterior = 1

while termos > 0:
    print(resultado, end=" → ")
    resultado = termo_atual + termo_anterior
    termo_anterior = termo_atual
    termo_atual = resultado
    termos -= 1
    
print("FIM")
print("~"*30)

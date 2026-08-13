'''
Faça um programa que mostre a tabuada de vários números, um de
cada vez, para cada valor digitado pelo usuário. O programa
sreá interrompido quano o número solicitado for negativo.
'''

valor = int(input("Quer ver a tabuada de qual valor? "))

while True:
    print("-"*30)
    c = 1
    while True:
        if c == 11:
            break
        print(f"{valor} x {c} = {valor * c}")
        c += 1
    print("-"*30)
    valor = int(input("Quer ver a tabuada de qual valor? "))
    if valor < 0:
        break
print("PROGRAMA DE TABUADA ENCERRADO. Volte sempre!")
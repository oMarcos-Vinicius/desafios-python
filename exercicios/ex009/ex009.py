#Fazer uma tabuada

numero = int(input("Digite um numero para saber sua tabuada do 10: "))
contador = 1

print("--------------")

while contador <= 10:
    print(f"{numero} x {contador:2} = {numero*contador}")
    contador += 1

print("--------------")
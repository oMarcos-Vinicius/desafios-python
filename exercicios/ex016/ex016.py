#Usar o math para separa a parte inteira da fracionada
from math import trunc

num = float(input("Digite um número: "))

print(f"O valor digitado foi {num} e a sua parte inteira é : {trunc(num)}")
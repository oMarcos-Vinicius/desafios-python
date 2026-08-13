'''
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, 
desconsiderando os espaços
'''
from unidecode import unidecode

frase = str(unidecode(input("Digite uma frase: "))).strip().upper()
frase = frase.replace(" ","")
frase_invertida = ""

for letra in range((len(frase)-1),-1,-1):
    frase_invertida += frase[letra]

#Com tratamento de string:
invertido = frase[::-1]
print(f"Usando o tratamento de string: {invertido}")

print(f"O inverso de {frase} é {frase_invertida}")

if frase == frase_invertida:
    print("Temos um palíndomo")
else:
    print("A frase digitada não é um palíndromo")

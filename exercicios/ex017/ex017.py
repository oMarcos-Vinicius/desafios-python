#Calcular a hipotenusa
from math import hypot

cat_oposto = float(input("Comprimento do cateto oposto: "))
cat_adjacente = float(input("Comprimento do cateto adjacente: "))

hipotenusa = hypot(cat_oposto, cat_adjacente)

print(f"A hipotenusa vai medir: {hipotenusa:.2f}")
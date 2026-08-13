# Conversor para o dolar

real = float(input('Quanto dinheiro você tem na carteira? R$'))

dolar = real / 4.99 #Cotação atual do dolar 1 dolar para 4,99 reais.

print(f"Com R${real:.2f} você pode comprar US${dolar:.2f}")
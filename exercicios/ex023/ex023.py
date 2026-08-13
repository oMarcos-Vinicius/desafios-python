numero = str(input("Informe um numero: "))

novo_numero = "0000" + numero

print(f"Analisando o numero {numero}")
print(f"Unidade: {novo_numero[-1]}")
print(f"Dezena: {novo_numero[-2]}")
print(f"Centena: {novo_numero[-3]}")
print(f"Milhar: {novo_numero[-4]}")
dias = int(input("Quantos dias alugados? "))
km = float(input("Quantos KM rodados? "))

# R$60 por dia + R$0,15 por KM

custo = (dias * 60) + (km * 0.15)

print(f"O total a pagar é de R${custo:.2f}")
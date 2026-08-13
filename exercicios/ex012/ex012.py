preco = float(input("Qual é o preço do produto: R$"))
preco_ofertado = preco - (preco * 0.05)

print(f"O produto custava R${preco:.2f}. Na promoção com desconto de 5%, vai custar R${preco_ofertado:.2f}")
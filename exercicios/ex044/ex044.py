'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu 
preço normal e a condição de pagamento:

- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preso normal
- 3x ou mais no cartão: 20% de juros
'''
print("="*10,"LOJAS GUANABARA","="*10)

preco = float(input("Preço das compras: R$"))

print("FORMAS DE PAGAMENTO")
print("[1] à vista dinheiro/cheque")
print("[2] à vista no cartão")
print("[3] em até 2x no cartão")
print("[4] 3x ou mais no cartão")

option = int(input("Qual á a opção? "))

if option == 1:
    valor_final = preco - (preco * 0.10)
    print(f"Sua compra de R${preco:.2f} vai custar R${valor_final:.2f} no final")
elif option == 2:
    valor_final = preco - (preco * 0.05)
    print(f"Sua compra de R${preco:.2f} vai custar R${valor_final:.2f} no final")
elif option == 3:
    valor_final = preco
    parcelas = int(input("Quantas parcelas?"))
    print(f"Sua compra será parcelada em {parcelas}x de R${(valor_final/parcelas):.2f} SEM JUROS")
    print(f"Sua compra vai custar R${valor_final:.2f} no final")
elif option == 4:
    valor_final = preco + (preco * 0.20)
    parcelas = int(input("Quantas parcelas?"))
    print(f"Sua compra será parcelada em {parcelas}x de R${valor_final/parcelas:.2f} COM JUROS")
    print(f"Sua compra de R${preco:.2f} vai custar R${valor_final:.2f} no final")
else:
    print("OPÇÃO INVÁLIDA! Comece novamente.")

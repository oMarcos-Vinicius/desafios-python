#Calcular a area em m² e descobrir a quantidade de tinta em litros. 
#Detalhes: para cada 2m² é necessarios 1l de tinta.

largura = float(input("Largura da parede: "))
altura = float(input("Altura da parede: "))

area = largura * altura
tinta_necessaria = area / 2

print(f"Sua parede tem uma dimensão de {largura:.2f}X{altura:.2f} e sua area é de {area:.2f}m²")
print(f"Para pintar essa parede, você precisará de {tinta_necessaria:.2f}l de tinta")

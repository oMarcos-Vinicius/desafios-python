'''
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calule o preço da passagem, cobrando R$ 0,50 por Km para viagens de 
até 200Km e R$ 0,45 para viagens mais longas. 
'''

distancia = float(input("Qual é a distância da sua vigem? "))

#Com if convencional:

if distancia <= 200:
    print(f"Você está prestes a começar uma viagem de {distancia:.1f}Km.")
    print(f"E o preço da sua pasagem será de R${(distancia*0.50):.2f}")
else:
    print(f"Você está prestes a começar uma viagem de {distancia:.1f}Km.")
    print(f"E o preço da sua pasagem será de R${(distancia*0.45):.2f}")

#Com if simplificado

preco = (distancia*0.50) if distancia <= 200 else (distancia*0.45)
print(f"Você está prestes a começar uma viagem de {distancia:.1f}Km.")
print(f"E o preço da sua pasagem será de R${preco:.2f}")
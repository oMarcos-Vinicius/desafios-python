'''
Faça um programa que tenha uma função chamada area(), que erceba as dimensões
de um terreno retangular (largura e comprimento) e mostre a area do terreno
'''
def area(largura, comprimento):
    area = largura * comprimento
    print(f"A área de um terreno {largura:.1f}x{comprimento:.1f} é de {area:.1f}m²")


print(f"{"Controle de Terenos":^30}")
print("-"*30)

lgr = float(input("LARGURA (m): "))
comp = float(input("COMPRIMENTO (m): "))

area(lgr, comp)
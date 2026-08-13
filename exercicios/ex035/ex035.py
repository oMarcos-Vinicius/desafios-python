'''
Desenvolva um programa que leia o comprimento de três retas e diga ao 
usuário se elas podem ou não formar um triângulo

*-*-*-*-*
Para verificar se três segmentos de reta podem formar um triângulo, usamos a desigualdade triangular:
Fórmula:
Sejam os comprimentos a, b e c. Eles formam um triângulo se e somente se: a+b>c, a+c>b, b+c>a
Ou seja, a soma de quaisquer dois lados deve ser maior que o terceiro.
*-*-*-*-*
'''
print("-=" * 30)
print("Analisador de triângulo")
print("-=" * 30)

segmento1 = float(input("Primeiro segmento: "))
segmento2 = float(input("Segundo segmento: "))
segmento3 = float(input("Terceiro segmento: "))

if ((segmento1 + segmento2) > segmento3) and ((segmento1 + segmento3) > segmento2) and ((segmento2 + segmento3) > segmento1):
    print("Os segmentos acima PODEM FORMAR um triângulo")
else:
    print("Os segmentos acima NÃO PODEM FORMAR um triângulo")


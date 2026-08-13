'''
Crie um programa onde o usuário possa digitar cinco valores numéricos
e cadastre-os em uma lista, já na possição correta de inserção
(sem usar o sort()).
No final, mostre a lista ordenada na tela.
'''
valores = []

for c in range(0,5):
    numero = int(input("Digite um valor: "))

    if c == 0 or numero > valores[-1]:
        valores.append(numero)
        print("Adicionado ao final da lista...")
    else:
        for pos, valor in enumerate(valores):
            if numero <= valor:
                valores.insert(pos, numero)
                print(f"Adicionado na posição {pos} da lista...")
                break

print("-="*30)
print("Os valores digitado em ordem foram",valores)
        
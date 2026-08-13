'''
Crie um programa onde o usuário digite uma expressão qualquer que use
parênteses. Seu aplicativo deverá analisar se a expressão passada
está com os parênteses abertos e fechado na ordem correta.
'''

expressao = str(input("Digite a expressão: "))
pilha = []

for caracter in expressao:
    if caracter == "(":
        pilha.append(caracter)
    elif caracter == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(caracter)
            break

if len(pilha) == 0:
    print("Sua expressão é válida!")
else:
    print("Sua expressão não é valida!")
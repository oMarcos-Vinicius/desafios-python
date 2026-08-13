'''
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma
semelhante à função input() do Python, só que fazendo a validação para aceitar
apenas um valor númerico.
'''

def leiaInt(texto):
    num = str(input(texto))

    while not num.isnumeric():
        print("\33[31mERRO! Digite um número inteiro válido. \33[m")
        num = input(texto)

    return int(num)

print("-" * 30)
n = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número {n}")
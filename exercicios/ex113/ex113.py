'''
Reescreva a função leiaInt() que fizemos no desario 104, incluindo agora
a possibilidade da digitação de um número de tipo inválido. Aprovite e crie
também uma função leiaFloat() com a mesma funcionalidade.
'''

def leiaInt(texto):
    while True:
        try:
            num = int(input(texto))
        except KeyboardInterrupt:
            print("\n\33[31mUsuário preferiu não digitar o valor\33[m")
            return 0
        except (ValueError, TypeError):
            print("\33[31mERRO! Digite um número inteiro válido. \33[m")
        else:
            return num

def leiaFloat(texto):
    while True:
        try:
            num = float(input(texto))
        except KeyboardInterrupt:
            print("\n\33[31mUsuário preferiu não digitar o valor\33[m")
            return 0
        except (TypeError, ValueError):
            print("\33[31mERRO! Digite um número real válido. \33[m")
        else:
            return num


print("-" * 30)
inteiro = leiaInt("Digite um número inteiro: ")
real = leiaFloat("Digite um número real: ")
print(f"Você acabou de digitar o número inteiro {inteiro} e o numero real {real}")
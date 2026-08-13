def dobro(valor=0):
    dobrado = valor * 2
    return dobrado

def metade(valor=0):
    meio = valor / 2
    return meio

def aumentar(valor=0, porcentagem=10):
    aumento = valor + (valor * (porcentagem / 100))
    return aumento

def diminuir(valor=0, porcentagem=10):
    reducao = valor - (valor * (porcentagem / 100))
    return reducao

def moeda(valor=0, cifra="R$"):
    return f"{cifra}{valor:.2f}".replace('.', ',')

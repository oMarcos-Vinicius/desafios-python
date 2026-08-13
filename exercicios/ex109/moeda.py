def dobro(valor=0, monetario=False):
    dobrado = valor * 2
    if monetario:
        return moeda(dobrado)
    return dobrado

def metade(valor=0, monetario=False):
    meio = valor / 2
    if monetario:
        return moeda(meio)
    return meio

def aumentar(valor=0, porcentagem=10, monetario=False):
    aumento = valor + (valor * (porcentagem / 100))
    if monetario:
        return moeda(aumento)
    return aumento

def diminuir(valor=0, porcentagem=10, monetario=False):
    reducao = valor - (valor * (porcentagem / 100))
    if monetario:
        return moeda(reducao)
    return reducao

def moeda(valor=0, cifra="R$"):
    return f"{cifra}{valor:.2f}".replace('.', ',')

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

def resumo(valor=0, aumento=10, desconto=10):
    print("-"*40)
    print("RESUMO DO VALOR".center(40))
    print("-"*40)
    print(f"Preço analisado: \t{moeda(valor):8}")
    print(f"Dobro do preço: \t{dobro(valor, True):8}")
    print(f"Metade do preço: \t{metade(valor, True):8}")
    print(f"{aumento}% de aumento: \t{aumentar(valor, aumento, True):8}")
    print(f"{desconto}% de redução: \t{diminuir(valor, desconto, True):8}")
    print("-"*40)


def leiaDinheiro(msg):
    valor = str(input(msg)).strip().replace(",",".")

    validar = valor.replace(".","",1)

    while validar.isnumeric() == False:
        print(f"\033[31mERRO: {valor} não é um preço invalido\033[m")
        valor = str(input(msg)).strip().replace(",",".")
        validar = valor.replace(".","")
    
    return float(valor)


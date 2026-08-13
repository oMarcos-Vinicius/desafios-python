'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
O programa vai perguntar o valor da casa, o sálario do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário 
ou então o empréstimo será negado.

Tabela ANSI
cores: 
\033[0m	Reset (volta ao padrão)	print("\033[0mNormal")
\033[1m	Negrito	print("\033[1mNegrito\033[0m")
\033[2m	Fraco (dim)	print("\033[2mDim\033[0m")
\033[3m	Itálico	print("\033[3mItálico\033[0m")
\033[4m	Sublinhado	print("\033[4mSublinhado\033[0m")
\033[7m	Inversão (texto ↔ fundo)	print("\033[7mInvertido\033[0m")
\033[9m	Tachado	print("\033[9mTachado\033[0m")

Código	Cor	Exemplo
\033[30m	Preto	print("\033[30mPreto\033[0m")
\033[31m	Vermelho	print("\033[31mVermelho\033[0m")
\033[32m	Verde	print("\033[32mVerde\033[0m")
\033[33m	Amarelo	print("\033[33mAmarelo\033[0m")
\033[34m	Azul	print("\033[34mAzul\033[0m")
\033[35m	Magenta	print("\033[35mMagenta\033[0m")
\033[36m	Ciano	print("\033[36mCiano\033[0m")
\033[37m	Branco	print("\033[37mBranco\033[0m")

Código	Cor de fundo	Exemplo
\033[40m	Preto	print("\033[40mFundo Preto\033[0m")
\033[41m	Vermelho	print("\033[41mFundo Vermelho\033[0m")
\033[42m	Verde	print("\033[42mFundo Verde\033[0m")
\033[43m	Amarelo	print("\033[43mFundo Amarelo\033[0m")
\033[44m	Azul	print("\033[44mFundo Azul\033[0m")
\033[45m	Magenta	print("\033[45mFundo Magenta\033[0m")
\033[46m	Ciano	print("\033[46mFundo Ciano\033[0m")
\033[47m	Branco	print("\033[47mFundo Branco\033[0m")
'''

casa = float(input("Valor da casa: R$"))
salario = float(input("Salário do comprador: R$"))
anos = int(input("Quantos anos de financiamento: "))
prestacao = casa / (anos*12)

print(f"Para para uma casa de R${casa:.2f} em {anos} anos, a prestação será de R${prestacao:.2f}")
if prestacao <= (salario * 0.30):
    print("Emprestimo pode ser \033[0;32;40m CONCEDIDO! \033[m")
else:
    print("Emprestimo \033[0;31;40m NEGADO! \033[m")
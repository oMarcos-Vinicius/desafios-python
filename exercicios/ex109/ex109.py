'''
Modifique as funções que forma criadas no desafio 107 para que elas aceitem
um parametro a mais, informando se o valore retornado por elas vai ser ou não
formatado pela função moeda(), desenvolvida no desafio 108.
'''
import moeda

preco = float(input("Digite um preço: R$"))

print(f"A metade de {moeda.moeda(preco, "US$")} é {moeda.metade(preco, True)}")
print(f"O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}")
print(f"Aumentando 10%, temos {moeda.aumentar(preco, 10)}")
print(f"Reduzindo 13%, temos {moeda.diminuir(preco, 13, False)}")
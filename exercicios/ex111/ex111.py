'''
Crie um pacote chamado utilizadadesCeV que tenha dois módulos internos chamados
moeda e dado

Transfira todas as funções utilizadas nos desafios 107, 108, 109 e 110 para o 
primeiro pacote e mantenha funcionando.
'''

from utilidadescev import moeda

preco = float(input("Digite um preço: R$"))
moeda.resumo(preco, 80, 35)
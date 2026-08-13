'''
Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo
chamado dado. Crie uma função chamado leiaDinheiro() que seja capaz de
funcionar como a função input(), mas com uma validação de daos para 
aceitar apenas valores que sejam monetário.
'''

from utilidadescev import moeda
from utilidadescev import dado

preco = dado.leiaDinheiro("Digite um preço: R$")
moeda.resumo(preco, 80, 35)
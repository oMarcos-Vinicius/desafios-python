'''
Crie um tupla preeenchida com os 20 primeiros colocados da
tabela do campeonato Brasileiro de Futebol, na ordem de
colocação. Depois, mostre:

a) Apenas os 5 primeiros colocados.
b) Os últimos 4 colocados da tabela.
c) Uma lista com os times em ordem alfabética.
d) Em que posição na tabela está o time da Chapecoense.
'''
times_brasileirao = (
    "Palmeiras", "Flamengo", "Fluminense", "Athletico Paranaense",
    "Red Bull Bragantino", "Bahia", "Coritiba", "São Paulo",
    "Atlético Mineiro", "Corinthians", "Cruzeiro", "Botafogo",
    "Vitória", "Internacional", "Santos", "Grêmio",
    "Vasco da Gama", "Remo", "Mirassol", "Chapecoense"
)

print("-="*40)
print(f"Lista dos times do Brasileirão: {times_brasileirao}")
print("-="*40)
print(f"a) Os 5 primeiros são: {times_brasileirao[0:5]}")
print("-="*40)
print(f"b) Os 4 últimos são: {times_brasileirao[-4:]}")
print("-="*40)
print(f"c) Times em ordem alfabética: {sorted(times_brasileirao)}")
print("-="*40)
print(f"d) A Chapecoense está na {times_brasileirao.index("Chapecoense")+1}º posição")
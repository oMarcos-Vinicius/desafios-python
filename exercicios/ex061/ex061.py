'''
Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros teremos da progressão usando a 
estrutura while
'''
print("="*30)
print("    ", "10 TERMOS DE UMA PA", "  ")
print("="*30)

primeiro_termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
contador = 0
#decimo = primeiro_termo + (10 - 1) * razao

while contador < 10:
    print(primeiro_termo, end=" → ")
    primeiro_termo += razao
    contador += 1

print("FIM")

'''
Melhore o DESAFIO 061, perguntando para o usuário se ele quer
mostrar mais alguns termos, o programa encerra quano ele disser
que quer mostrar 0 termos.
'''
print("="*30)
print("    ", "10 TERMOS DE UMA PA", "  ")
print("="*30)

primeiro_termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
contador = 0
continuar = 10
termos = 0

while continuar != 0:
    termos += continuar
    while contador < continuar:
        print(primeiro_termo, end=" → ")
        primeiro_termo += razao
        contador += 1
    print("PAUSA")
    contador = 0
    continuar = int(input("Quantos temos você quer mostrar a mais? "))

print(f"Progressão finalizada com {termos} termos mostrados")
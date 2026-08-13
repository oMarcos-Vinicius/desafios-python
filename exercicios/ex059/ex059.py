'''
Crie um programa que leia dois valores e mostre um menu na tela:
[1] Somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''
from time import sleep

valor1 = int(input("Primeiro valor: "))
valor2 = int(input("Segundo valor: "))

end = False

while not end:
    print("""    [1] Somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa""")
    option = int(input(">>> Qual é a sua opção? "))

    if option == 1:
        print(f"A soma entre {valor1} + {valor2} é {valor1+valor2}")
    elif option == 2:
        print(f"A multiplicação entre {valor1} X {valor2} é {valor1*valor2}")
    elif option == 3:
        if valor1 > valor2:
            print(f"Entre {valor1} e {valor2} o maior é {valor1}")
        else:
            print(f"Entre {valor1} e {valor2} o maior é {valor2}")
    elif option == 4:
        valor1 = int(input("Primeiro valor: "))
        valor2 = int(input("Segundo valor: "))
    elif option == 5:
        print("Finalizando...")
        end = True
    else:
        print("Opção inválida! Tente novamente.")
    
    print("=-" *20)
    sleep(2)

print("Fim do programa! Volte sempre!")
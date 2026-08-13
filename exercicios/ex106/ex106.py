'''
Faça um mini-sistema que ultilize o Interactive Help do Python. O usuário vai 
digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra
"FIM", o programa se encerrará.
'''


def pyHelp():
    from time import sleep

    while True:
        titulo = " SISTEMA DE AJUDA PYHELP "
        print(f"\033[0;30;42m")
        print("~" * len(titulo))
        print(titulo)
        print("~" * len(titulo), f"\033[m")

        resp = str(input("Função ou biblioteca > "))

        if resp.upper().strip() in "FIM":
            break

        msg = " Acessando o manual do comando '" + resp + "' "
        print(f"\033[0;30;44m")
        print("~" * len(msg))
        print(msg)
        print("~" * len(msg), f"\033[0;30;47m")
        sleep(1)
        help(resp)

    saida = " ATÉ LOGO! "
    print(f"\033[0;30;41m")
    print("~" * len(saida))
    print(saida)
    print("~" * len(saida), f"\033[m")

pyHelp()
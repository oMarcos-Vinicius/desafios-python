'''
Crie um programa que tenha uma função fatorial() que recebe dois parametros: o primeiro
que indique o número a calcular e o outro chamado show, que será um valor lógico
(opcional) indicando se será mostrado ou não na tela o processo de cálculo do
fatorial.
'''

def fatorial(numero, show=False):
    """Calcula o Fatorial de um número

    Args:
        numero (int): número a ser calculado
        show (bool, optional): Mostrar ou não a conta. Defaults to False.

    Returns:
        int: O valor do fatorial de um numero.
    """
    resultado = 1
    for c in range(numero, 0, -1):
        resultado *= c
        if show:
            if c == 1:
                print(f"{c}", end=" = ")
            else:
                print(f"{c}", end=" X ")
    return resultado


print(fatorial(5, True))
help(fatorial)
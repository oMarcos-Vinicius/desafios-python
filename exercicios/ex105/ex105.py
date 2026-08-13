'''
Faça um programa que tenha uma função notas() que pode receber várias notas
de um aluno e vai retornar um dicionário com as seguinte informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione també as docstings da função.
'''

def notas(*notas, situacao=False):
    """Função para analisar notas e situações de vários alunos.

    Args:
        *notas: Uma sequencia de valores ou notas. 
        situacao (bool, optional): indica se deve ou não retornar a situação de acordo com a notas. Defaults to False.

    Returns:
        dict: retonar um dicionário contendo total de notas, a maior e menor nota, a média e a situação(ops) do aluno
    """
    resultado = {
        'total' : len(notas),
        'maior' : max(notas),
        'menor' : min(notas),
        'media' : round(sum(notas) / len(notas), 2)
        }

    if situacao:
        if resultado['media'] >= 7:
            resultado['situação'] = "BOM"
        elif resultado['media'] >= 5:
            resultado['situação'] = "REGULAR"
        else:
            resultado['situação'] = "RUIM"

    return resultado


resp = (notas(10, 10, 10, 2, 7, 4, situacao=True))
print(resp)
help(notas)
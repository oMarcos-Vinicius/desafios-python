'''
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro
o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma
pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
'''

def voto(ano_nascimento):
    from datetime import date

    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento

    if (idade < 16):
        return (f"Com {idade} anos: VOTO NEGADO")
    elif (idade < 18) or (idade > 64):
        return (f"Com {idade} anos: VOTO OPCIONAL")
    else:
        return (f"Com {idade} anos: VOTO OBRIGATORIO")
    

print("-" * 40)
print(voto(int(input("Em que ano você nasceu? "))))

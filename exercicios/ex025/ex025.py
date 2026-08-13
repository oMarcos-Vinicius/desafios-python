from unidecode import unidecode

nome = str(input("Qual é o seu nome completo? "))

nome = unidecode(nome.strip().upper())

print("SILVA" in nome)

full_name = str(input("Digite seu nome completo: "))
first_name = full_name.split()

print("Analisando o seu nome...")

print(f"Seu nome em maiúscula é {full_name.upper()}")
print(f"Seu nome em minúscula é {full_name.lower()}")
print(f"Seu nome tem ao todo {len(full_name) - full_name.count(" ")} letras")
print(f"Seu primeiro nome é {first_name[0]} {len(first_name[0])}")

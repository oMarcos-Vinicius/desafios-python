from unidecode import unidecode

cidade = unidecode(str(input("Em que cidade você nasceu? "))).strip().lower()

print(f"Sua cidade começa com Santo?: {cidade[:5] == "santo"}")

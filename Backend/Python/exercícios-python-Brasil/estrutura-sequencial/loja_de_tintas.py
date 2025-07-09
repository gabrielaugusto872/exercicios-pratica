# Autor: Gabriel Augusto dos Santos
# Data: 2025-07-09

area = float(input("Digite em metros quadrados a área que será pintada: "))

latas = area / (18 * 3)
preco_total  = latas * 80

print(f"Devem ser compradas {latas} latas que terão um preço total de {preco_total} reais.")

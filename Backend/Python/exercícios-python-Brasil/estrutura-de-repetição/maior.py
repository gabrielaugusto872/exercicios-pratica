# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-08
# Exercício:   Faça um programa que leia 5 números e informe o maior número.

maior = None

for i in range(5):
    numero = float(input(f"Digite o {i+1}° número: "))

    if i == 0 or numero > maior:
        maior = numero

print(f"Maior: {maior}")
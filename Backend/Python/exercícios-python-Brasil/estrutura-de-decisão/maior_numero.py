# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-06
# Exercício: Faça um programa que peça dois números e imprima o maior deles.

maior = 0

numero_1 = float(input("Digite o primeiro número: "))
numero_2 = float(input("Digite o segundo número: "))

if numero_1 > numero_2:
    maior = numero_1
elif numero_2 > numero_1:
    maior = numero_2

print(f"O maior número é: {maior}")
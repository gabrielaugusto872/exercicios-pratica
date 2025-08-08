# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-07
# Exercício: Faça um programa que peça um número inteiro e determine se ele é par ou impar.

numero = int(input("Digite o numero: "))

if numero % 2 == 0:
    print(f"O número {numero} é par!")
else:
    print(f"O número {numero} é impar")
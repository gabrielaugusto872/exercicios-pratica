# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-07
# Exercício: Faça um programa que peça um número e informe se o número é inteiro ou decimal.

numero = input("Digite o número: ")

if float(numero) == int(float(numero)):
    print(f"{numero} é um número inteiro.")
else:
    print(f"{numero} é um número decimal")
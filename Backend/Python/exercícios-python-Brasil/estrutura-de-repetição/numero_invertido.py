# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-13
# Exercício: Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.

numero = input()
tamanho = len(numero)

for i in range(tamanho-1,-1,-1):
    print(numero[i], end="")
print()
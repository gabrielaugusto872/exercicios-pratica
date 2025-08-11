# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-11
# Exercício: Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

numero_1 = int(input("Digite o 1° número: "))
numero_2 = int(input("Digite o 2° número: "))

for i in range(numero_1 + 1, numero_2):
    print(i, end="\n")
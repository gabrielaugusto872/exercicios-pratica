# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-06
# Exercício: Faça um programa que leia três números e mostre o maior deles

maior = 0

numero_1 = float(input("Digite o primeiro número: "))
numero_2 = float(input("Digite o segundo número: "))
numero_3 = float(input("Digite o terceiro número: "))

if numero_1 > numero_2:
    maior = numero_1
elif numero_2 > numero_1:
    maior = numero_2

if numero_3 > maior:
        maior = numero_3

print(maior)
# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-06
# Exercício: Faça um programa que leia três números e mostre o maior e o menor deles.

maior = 0
menor = 0

numero_1 = float(input("Digite o primeiro número: "))
numero_2 = float(input("Digite o segundo número: "))
numero_3 = float(input("Digite o terceiro número: "))

if numero_1 > numero_2:
    maior = numero_1
    menor = numero_2
elif numero_2 > numero_1:
    maior = numero_2
    menor = numero_1

if numero_3 > maior:
        maior = numero_3
elif numero_3 < maior:
     if numero_3 < menor:
          menor = numero_3

print(f"Maior: {maior}\nMenor: {menor}")
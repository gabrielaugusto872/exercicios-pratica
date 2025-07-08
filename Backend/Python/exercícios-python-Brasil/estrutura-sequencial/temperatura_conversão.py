# Autor: Gabriel Augusto dos Santos
# Data: 2025-07-08
# Exercício: Faça um programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))

celsius = 5 * ((fahrenheit - 32) / 9)
print(f"{fahrenheit} graus Fahrenheit é equivalente a {celsius} graus Celsius.")
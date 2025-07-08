# Autor: Gabriel Augusto dos Santos
# Data: 2025-07-08
# Exercício: Faça um programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

celsius = float(input("Digite a temperatura em graus Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32
print(f"{celsius} graus Celsius é equivalente a {fahrenheit} graus Fahrenheit.")
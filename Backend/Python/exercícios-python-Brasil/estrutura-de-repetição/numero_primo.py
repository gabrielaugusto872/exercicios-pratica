# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-11
# Exercício: Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

numero = int(input("Digite o número: "))

if numero < 2:
    print(f"{numero} não é primo.")
else:
    testa = 0
for i in range(2, numero):
    if numero % i == 0:
        testa += 1

if testa == 0:
    print(f"{numero} é primo.")
else:
    print(f"{numero} não é primo.")

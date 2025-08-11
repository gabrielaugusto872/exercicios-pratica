# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-11
# Exercício: Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.

fatorial = 1

numero = int(input("Digite um número: "))

print(numero, end="!=")
for i in range(numero, 0, -1):
    if i > 1:
        print(i, end=".")
        fatorial *= i
    else:
        print(i, end="=")

print(fatorial)
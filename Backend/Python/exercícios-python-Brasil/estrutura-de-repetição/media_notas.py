# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-12
# Exercício: Faça um programa que calcule o mostre a média aritmética de N notas.

n = int(input("Digite quantas notas serão inseridas: "))

soma = 0

for i in range(n):
    notas = float(input(f"Digite a {i+1}° nota: "))
    soma += notas

media = soma/n

print(f"Média: {media}")
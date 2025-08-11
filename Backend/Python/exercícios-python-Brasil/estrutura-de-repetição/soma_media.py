# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-11
# Exercício: Faça um programa que leia 5 números e informe a soma e a média dos números.

contagem = 0
soma = 0

while contagem < 5:
    numero = int(input(f"Digite o {contagem + 1}° número: "))
    soma += numero
    contagem += 1

media = soma / 5

print(f"Soma: {soma}\nMédia: {media}")

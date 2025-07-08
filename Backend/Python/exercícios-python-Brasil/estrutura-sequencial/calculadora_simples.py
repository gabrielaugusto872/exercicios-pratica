# Autor: Gabriel Augusto dos Santos
# Data: 2025-07-08
# Exercício: Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:
#            -> O produto do dobro do primeiro com metade do segundo.
#            -> A soma do triplo do primeiro com o terceiro.
#            -> O terceiro elevado ao cubo.

inteiro_1 = int(input("Digite o primeiro número inteiro: "))
inteiro_2 = int(input("Digite o segundo número inteiro: "))
numero_real = float(input("Digite o número real: "))

produto = (inteiro_1 * 2) * (inteiro_2 / 2)
soma = (inteiro_1 * 3) + numero_real
cubo = numero_real ** 3

print(f"O produto do dobro do primeiro número com metade do segundo número é: {produto}")
print(f"A soma do triplo do primeiro número com o terceiro número é: {soma}")
print(f"O terceiro número elevado ao cubo é: {cubo}")
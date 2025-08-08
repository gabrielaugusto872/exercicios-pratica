# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-08
# Exercício: Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

populacao_a = 80000
taxa_a = 0.03
populacao_b = 200000
taxa_b = 0.015
ano = 0

while populacao_a  < populacao_b:
    populacao_a += populacao_a * taxa_a
    populacao_b += populacao_b * taxa_b
    ano += 1

print(f"A população de A ultrapassará B em {ano} anos.")
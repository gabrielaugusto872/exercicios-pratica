# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-12
# Exercício: Desenvolva um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

quantidade = 0
soma = 0

temperaturas = float(input(f"Digite a {quantidade+1}° temperatura: "))

maior = temperaturas
menor = temperaturas

while temperaturas != -9999:
    quantidade += 1
    soma += temperaturas

    if temperaturas > maior:
        maior = temperaturas
    elif temperaturas < menor:
        menor = temperaturas

    temperaturas = float(input(f"Digite a {quantidade+1}° temperatura: "))

media = soma / quantidade


print(f"Maior temperatura: {maior}")
print(f"Menor temperatura: {menor}")
print(f"Média das temperaturas: {media:.2f}")
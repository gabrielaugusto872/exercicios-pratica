# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-11
# Exercício: Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

pares = ""
contagem_pares = 0
impares = ""
contagem_impares = 0

for contagem in range(10):
    numeros = int(input(f"Digite o {contagem + 1}° número: "))
    if numeros % 2 == 0:
        pares += str(numeros) + ", "
        contagem_pares +=1
    else:
        impares += str(numeros) + ", "
        contagem_impares +=1

print(f"{contagem_pares} pares: {pares}")
print(f"{contagem_impares} ímpares: {impares}")
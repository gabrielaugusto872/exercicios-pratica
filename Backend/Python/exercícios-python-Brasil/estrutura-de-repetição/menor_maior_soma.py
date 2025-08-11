# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-11
# Exercício: Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

n = int(input("Quantos números serão inseridos? "))

for i in range(n):
    if i == 0:
        numero = float(input(f"Digite o {i+1}° número: "))
        menor = numero
        maior = numero
        soma = numero
    else:
        numero = float(input(f"Digite o {i+1}° número: "))
        soma += numero
        if numero < menor:
            menor = numero
        elif numero > maior:
            maior = numero

print(f"""Maior: {maior}
Menor: {menor}
Soma: {soma}""")
        
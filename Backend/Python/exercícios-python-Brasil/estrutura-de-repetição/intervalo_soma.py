# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-11
# Exercício: Altere o programa anterior para mostrar no final a soma dos números.

soma = 0

numero_1 = int(input("Digite o 1° número: "))
numero_2 = int(input("Digite o 2° número: "))

for i in range(numero_1 + 1, numero_2):
    print(i, end="\n")
    soma += i

print(f"Soma: {soma}")
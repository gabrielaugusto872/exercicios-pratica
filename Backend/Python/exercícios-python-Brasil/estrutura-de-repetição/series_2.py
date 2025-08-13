# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-13
# Exercício: Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.

serie = "H = "

n = int(input())

for i in range(n):
    if i == 0:
        serie += "1"
        soma = 1
    else:
        serie += f" + 1/{i+1}"
        soma += (1/(i+1))

print()
print(f"{serie} = {soma:.2f}")
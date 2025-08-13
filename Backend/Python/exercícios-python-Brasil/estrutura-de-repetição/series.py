# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-13
# Exercício: Faça um programa que mostre os n termos da Série a seguir:
#            S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
#            Imprima no final a soma da série.

serie = "S = "
n = int(input())

for i in range(n):
    if i == 0:
        serie += "1/1"
        soma = 1
    else:
        a = (i+1) + i
        serie += f" + {i+1}/{a}"
        soma += ((i+1)/a)
print()
print(f"{serie} = {soma:.2f}")
    
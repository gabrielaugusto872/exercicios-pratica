# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-13
# Exercício: Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]

contagem_1 = 0
contagem_2 = 0
contagem_3 = 0
contagem_4 = 0

num = int(input("Digite números separados por enter: "))
while num >= 0:
    if num in range(0,26):
        contagem_1 += 1
    elif num in range(26,51):
        contagem_2 += 1
    elif num in range(51,76):
        contagem_3 += 1
    elif num in range(76,101):
        contagem_4 += 1

    num = int(input(""))

print(f"Números entre 0 e 25: {contagem_1}")
print(f"Números entre 26 e 50: {contagem_2}")
print(f"Números entre 51 e 75: {contagem_3}")
print(f"Números entre 76 e 100: {contagem_4}")

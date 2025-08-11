# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-11
# Exercício: Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número

base = float(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

if base == 0:
    print(f"{base} ** {expoente} = 0")
elif expoente == 0:
    print(f"{base} ** {expoente} = 1")
elif expoente == 1:
    print(f"{base} ** {expoente} = {base}")

conta = 1
for _ in range(expoente):
    conta *= base

print(f"{base} elevado a {expoente} = {conta}")
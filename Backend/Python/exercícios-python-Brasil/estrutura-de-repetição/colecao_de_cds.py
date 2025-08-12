# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-12
# Exercício: Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles.

valor_total = 0

quantidade = int(input("Digite a quantidade de CD's: "))

for i in range(quantidade):
    valor = float(input(f"Digite o valor do {i+1} CD: "))
    valor_total += valor

valor_medio = valor_total/quantidade

print(f"Valor total investido: {valor_total:.2f}")
print(f"Valor médio gasto em cada CD: {valor_medio:.2f}")
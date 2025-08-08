# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-07
# Exercício: Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

morangos = float(input("Digite a quantidade de morangos: "))
macas = float(input("Digite a quantidade de maçãs: "))

kg_totais = morangos + macas

if morangos <= 5:
    valor_morangos = morangos * 2.50
else:
    valor_morangos = morangos * 2.20

if macas <= 5:
    valor_macas = macas * 1.80
else:
    valor_macas = macas * 1.50

valor_total = valor_morangos + valor_macas

if valor_total > 25 or kg_totais > 8:
    valor_total = valor_total - (valor_total * 0.10)

print(f"Valor a ser pago: {valor_total}")
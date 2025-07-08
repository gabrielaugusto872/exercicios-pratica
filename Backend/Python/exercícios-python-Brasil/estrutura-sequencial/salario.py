# Autor: Gabriel Augusto dos Santos
# Data: 2025-07-08
# Exercício: Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

ganho_hora = float(input("Digite quanto você ganha por hora: "))
horas_trabalhadas = float(input("Digite quantas horas você trabalhou nesse mês: "))

salario = ganho_hora * horas_trabalhadas
print(f"Seu salário esse mês deve ser {salario} reais.")

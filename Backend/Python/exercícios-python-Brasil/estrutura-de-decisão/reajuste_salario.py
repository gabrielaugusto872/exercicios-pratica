# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-06
# Exercício: Faça um programa que recebe o salário de um colaborador e o reajuste.

aumento = 0
valor_aumento = 0
salario_novo = 0

salario = float(input("""Digite o salário do colaborador em reais:
$"""))

if salario <= 280:
    aumento = 0.20
elif salario < 700:
    aumento = 0.15
elif salario < 1500:
    aumento = 0.10
else:
    aumento = 0.05

valor_aumento = salario * aumento
salario_novo = valor_aumento + salario

print(f"Salário antes do reajuste: ${salario}")
print(f"Percentual de aumento aplicado: {aumento*100:.0f}%")
print(f"Valor do aumento: ${valor_aumento}")
print(f"Novo salário: ${salario_novo}")
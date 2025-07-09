# Autor: Gabriel Augusto dos Santos
# Data: 2025-07-09

ganho_hora = float(input("DIgite o quanto você ganha por hora: "))
horas_trabalhadas = float(input("Digite o total de horas trabalhadas: "))

salario_bruto = ganho_hora * horas_trabalhadas
print(f"Salário Bruto: {salario_bruto}")

imposto_de_renda = salario_bruto * 0.11

inss = salario_bruto * 0.08
print(f"Pago ao INSS: {inss}")

sindicato = salario_bruto * 0.05
print(f"Pago ao Sindicato: {sindicato}")

salario_liquido = salario_bruto - imposto_de_renda - inss - sindicato
print(f"Salário Líquido: {salario_liquido}")
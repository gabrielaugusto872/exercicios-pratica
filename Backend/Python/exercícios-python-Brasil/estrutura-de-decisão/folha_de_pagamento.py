# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-06
# Exercício: Faça um programa para o cálculo de uma folha de pagamento.

INSS = 0.10
FGTS = 0.11

salario_bruto = 0
salario_liquido = 0
imposto_de_renda = 0
descontos = 0

valor_hora = float(input("Digite o valor da sua hora de trabalho: "))
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))

salario_bruto = valor_hora * horas_trabalhadas

if salario_bruto <= 900:
    imposto_de_renda = 0
elif salario_bruto <= 1500:
    imposto_de_renda = 0.05
elif salario_bruto <= 2500:
    imposto_de_renda = 0.10
else:
    imposto_de_renda = 0.20

descontos = (salario_bruto * imposto_de_renda) + (salario_bruto * INSS)
salario_liquido = salario_bruto - descontos


print(f"""\nSalário Bruto: ({valor_hora:.0f}*{horas_trabalhadas:.0f})  : $ {salario_bruto:.2f}
(-) IR ({imposto_de_renda*100:.0f}%)             : $ {imposto_de_renda*salario_bruto:.2f}
(-) INSS (10%)          : $ {INSS*salario_bruto:.2f}
FGTS (11%)              : $ {FGTS*salario_bruto:.2f}
Total de descontos      : $ {descontos}
Salário Líquido         : $ {salario_liquido}\n""")
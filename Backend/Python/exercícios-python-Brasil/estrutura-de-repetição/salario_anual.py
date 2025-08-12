# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-12
# Exercício: Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.

ADMISSAO = 1995
ANO_ATUAL = 2025
PERCENTUAL_INICIAL = 0.015 # 1,5%

salario_inicial = float(input("Digite o salário inicial do funcionário: "))

anos_trabalhados = ANO_ATUAL - ADMISSAO

for i in range(anos_trabalhados):
    if i == 0:
        aumento = salario_inicial * PERCENTUAL_INICIAL
        salario = salario_inicial + aumento
        percentual = PERCENTUAL_INICIAL
        print(aumento)
        print(salario)
    else:
        percentual *= 2
        aumento = salario * percentual
        salario += aumento
        print(aumento)
        print(salario)

print(f"Salário atual: R$ {salario:.2f}")
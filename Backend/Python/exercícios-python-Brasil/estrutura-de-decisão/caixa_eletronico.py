# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-07
# Exercício: Faça um programa para um caixa eletrônico. 

saque = input("Digite o valor do saque: ")

if int(saque) < 10 or int(saque) > 600:
    print("""Valor mínimo: $ 10
Valor máximo: $ 600""")

else:
    restante = int(saque)

    nota_100 = restante // 100
    restante %= 100

    nota_50 = restante // 50
    restante %= 50

    nota_10 = restante // 100
    restante %= 10

    nota_5 = restante // 5
    restante %= 5

    nota_1 = restante

    print(f"\nPara sacar R$ {saque}, serão fornecidas:")

    if nota_100 > 0:
        print(f"{nota_100} nota{'s' if nota_100 > 1 else ''} de 100")
    if nota_50 > 0:
        print(f"{nota_50} nota{'s' if nota_50 > 1 else ''} de 50")
    if nota_10 > 0:
        print(f"{nota_10} nota{'s' if nota_10 > 1 else ''} de 10")
    if nota_5 > 0:
        print(f"{nota_5} nota{'s' if nota_5 > 1 else ''} de 5")
    if nota_1 > 0:
        print(f"{nota_1} nota{'s' if nota_1 > 1 else ''} de 1")
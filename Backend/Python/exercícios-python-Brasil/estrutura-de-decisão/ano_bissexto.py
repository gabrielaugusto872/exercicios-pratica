# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-06
# Exercício: Faça um programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

ano = int(input("Digite o ano: "))

if ano % 400 == 0:
    print(f"{ano} é um ano bissexto!")
elif ano % 4 == 0:
    if ano % 100 != 0:
        print(f"{ano} é um ano bissexto!")
    else:
        print(f"{ano} não é um ano bissexto!")
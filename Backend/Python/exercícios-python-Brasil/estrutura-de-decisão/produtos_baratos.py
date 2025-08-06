# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-06
# Exercício: Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

produto_1 = float(input("Digite o preço do primeiro produto: "))
produto_2 = float(input("Digite o preço do segundo produto: "))
produto_3 = float(input("Digite o preço do terceiro produto: "))

if produto_1 < produto_2 and produto_1 < produto_3:
    print(f"Compre o primeiro produto de $ {produto_1:.2f}.")
elif produto_2 < produto_1 and produto_2 < produto_3:
    print(f"Compre o segundo produto de $ {produto_2:.2f}.")
elif produto_3 < produto_2 and produto_3 < produto_2:
    print(f"Compre o terceiro produto de $ {produto_3:.2f}.")

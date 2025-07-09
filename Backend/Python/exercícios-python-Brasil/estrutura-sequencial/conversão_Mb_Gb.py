# Autor: Gabriel Augusto dos Santos
# Data: 2025-07-09
# Exercício: Tendo como dados de entrada um arquivo em Gigabytes, construa um algoritmo que faça a conversão para Megabytes.

gigabytes = float(input("Digite o tamanho do arquivo em Gigabytes: "))

megabytes = gigabytes * 1024

print(f"O arquivo tem {megabytes} Mbs.")
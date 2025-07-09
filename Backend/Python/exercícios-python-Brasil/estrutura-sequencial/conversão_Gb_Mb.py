# Autor: Gabriel Augusto dos Santos
# Data: 2025-07-09
# Exercício: Tendo como dados de entrada um arquivo em Gigabytes, construa um algoritmo que faça a conversão para Megabytes e Kilobytes, usando as seguintes fórmulas:
#            -> Para Megabytes: Gigabytes * 1024
#            -> Para Kilobytes: Gigabytes * 1024 * 1024
#            -> Responda o tamanho do arquivo em Megabytes e o tamanho em Kilobytes.

gigabytes = float(input("Digite o arquivo em Gigabytes: "))

megabytes = gigabytes * 1024
kilobytes = megabytes * 1024

print(f"O arquivo tem {megabytes} Mbs ou {kilobytes} Kbs.")
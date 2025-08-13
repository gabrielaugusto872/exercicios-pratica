# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-13
# Exercício: Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.

juros = 0

divida_inicial = float(input("Digite o valor da dívida: "))

valor_parcela = divida_inicial

print(f"{"Valor da Dívida":<15} | {"Valor dos Juros":<15} | {"Quantidade de Parcelas":<22} | {"Valor da Parcela":<20}")
print(f"{f"R$ {divida_inicial:.2f}":<15} | {f"{juros:.2f}":<15} | {f"1":<22} | {f"R$ {valor_parcela:.2f}":<15}")

for i in range(3,13,3):
    if i == 3:
        porcentagem = 0.10
    elif i == 6:
        porcentagem = 0.15
    elif i == 9:
        porcentagem = 0.20
    elif i == 12:
        porcentagem = 0.25

    juros = divida_inicial * porcentagem
    divida = divida_inicial + juros
    valor_parcela = divida / i

    print(f"{f"R$ {divida:.2f}":<15} | {f"{juros:.2f}":<15} | {f"{i}":<22} | {f"R$ {valor_parcela:.2f}":<15}")
print()
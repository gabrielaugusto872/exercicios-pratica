# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-08
# Exercício: Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

valor = 11

while True:
    valor = float(input("Digite o valor: "))

    if valor < 0 or valor > 10:
        print("Valor inválido!")
    else:
        break

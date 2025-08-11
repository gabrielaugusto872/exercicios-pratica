# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-11
# Exercício: Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

numero = int(input("Digite o número: "))

if numero < 2:
    print(f"{numero} não é primo.")
else:
    divisores = ""
    testa = 0
for i in range(2, numero):
    if numero % i == 0:
        testa += 1
        divisores += f"{i},"        

if testa == 0:
    print(f"{numero} é primo.")
else:
    print(f"{numero} não é primo, pois é divisível por: {divisores}")

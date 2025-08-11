# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-11
# Exercício: Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.

numero = 11

while numero > 10:
    numero = int(input("Digite o numero: "))
    if numero > 10:
        print("Digite um número entre 0 e 10.")

print(f"Tabuada de {numero}:")
for tabuada in range(1,11):
    conta = numero * tabuada
    print(f"{numero} X {tabuada} = {conta}")
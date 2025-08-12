# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-12
# Exercício: Faça um programa que peça para n pessoas a sua idade, ao final o programa devera calcular a media e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada

soma = 0

n = int(input("Digite o número de pessoas na turma: "))

for i in range(n):
    idade = int(input(f"Digite a idade da {i+1}° pessoa: "))
    soma += idade

media = soma/n

if media > 0 and media <= 25:
    print("A turma é jovem!")
elif media > 25 and media <= 60:
    print("A turma é adulta!")
else:
    print("A turma é idosa!")
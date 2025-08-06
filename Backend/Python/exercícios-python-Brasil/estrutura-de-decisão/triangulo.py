# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-06
# Exercício: Faça um programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

print("Digite o valor dos lados do suposto triângulo:")
lado_1 = float(input("1° lado: "))
lado_2 = float(input("2° lado: "))
lado_3 = float(input("3° lado: "))

if (lado_1 + lado_2) > lado_3 or (lado_1 + lado_3) > lado_2 or (lado_3 + lado_2) > lado_1:
    print("Esses valores podem formar um triângulo: ")
    if lado_1 == lado_2 and lado_1 == lado_3:
        print("Equilátero")
    elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
        print("Isósceles")
    else:
        print("Escaleno")
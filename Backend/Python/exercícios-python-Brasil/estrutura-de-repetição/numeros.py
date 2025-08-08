# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-08
# Exercício: Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.

opcao = int(input("""Escolha como deseja que a lista seja mostrada: 
1 - Um número abaixo do outro
2 - Um número do lado do outro
"""))

if opcao == 1:
    for numero in range(1,21):
        print(numero, end="\n")
    print()
elif opcao == 2:
    for numero in range(1,21):
        print(numero, end=" ")
    print()
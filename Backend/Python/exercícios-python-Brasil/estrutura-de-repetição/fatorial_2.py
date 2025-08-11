# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-11
# Exercício: Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16

while True:
    print("Deseja calcular um fatorial?(S/N)")
    opcao = input("").strip()

    if opcao.upper() == "S":
        numero = int(input("Digite um número: "))
        if numero < 0 or numero >= 16:
            print("Digite apenas números inteiros positivos e menores que 16")
        else:
            fatorial = 1
            print(numero, end="!=")
            for i in range(numero, 0, -1):
                if i > 1:
                    print(i, end=".")
                    fatorial *= i
                else:
                    print(i, end="=")
            print(fatorial)
    elif opcao.upper() == "N":
        break
    else:
        print("Digite apenas S ou N.")

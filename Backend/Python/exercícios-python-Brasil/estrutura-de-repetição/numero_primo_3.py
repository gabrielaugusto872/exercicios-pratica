# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-12
# Exercício: Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.

n = int(input("Digite até que numero voce deseja visualizar: "))

if n < 2:
        print(f"Não existem números primos de 1 até {n}")
else:
    divisões = 0
    primos = ""
    for numero in range(2, n + 1):
        testa = 0
        for i in range(2, numero):
            divisões += 1
            if numero % i == 0:
                testa += 1

        if testa == 0:
            primos += f"{numero}, "
    
    print(f"Números primos entre 1 e {n}: ")
    print(primos)
    print(f"Número de divisões executadas para encontrar esses números: {divisões}")

# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-07
# Exercício: Faça um programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.

while True:
    numero = (input("Digite o número: "))

    if numero == "2222": # BREAK: Digitar 2222
        break

    if int(numero) >= 1000 or int(numero) < 0:
        print ("Digite apenas números inteiros.")
    else:
        if len(numero) == 3:
            centena = int(numero[0])
            dezena = int(numero[1])
            unidade = int(numero[2])
        elif len(numero) == 2:
            centena = 0
            dezena = int(numero[0])
            unidade = int(numero[1])
        elif len(numero) == 1:
            centena = 0
            dezena = 0
            unidade = int(numero)

        if centena != 0:
            if dezena != 0:
                if unidade != 0:
                    print(f"{numero} = {centena} {"centena" if centena == 1 else "centenas"}, {dezena} {"dezena" if dezena == 1 else "dezenas"} e {unidade} {"unidade" if unidade == 1 else "unidades"}")
                else:
                    print(f"{numero} = {centena} {"centena" if centena == 1 else "centenas"} e {dezena} {"dezena" if dezena == 1 else "dezenas"}")
            else:
                if unidade != 0:
                    print(f"{numero} = {centena} {"centena" if centena == 1 else "centenas"} e {unidade} {"unidade" if unidade == 1 else "unidades"}")
                else:
                    print(f"{numero} = {centena} {"centena" if centena == 1 else "centenas"}")
        else:
            if dezena != 0:
                if unidade != 0:
                    print(f"{dezena} {"dezena" if dezena == 1 else "dezenas"} e {unidade} {"unidade" if unidade == 1 else "unidades"}")
                else:
                    print(f"{dezena} {"dezena" if dezena == 1 else "dezenas"}")
            else:
                if unidade != 0:
                    print(f"{unidade} {"unidade" if unidade == 1 else "unidades"}")
                else:
                    print(f"{numero} = 0")
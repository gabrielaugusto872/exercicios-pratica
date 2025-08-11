# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-11
# Exercício: Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

n = int(input("Quantos números serão inseridos? "))

for i in range(n):
    if i == 0:
        numero = float(input(f"Digite o {i+1}° número: "))
        while numero < 0 or numero > 1000:
            print("Valor inválido! Digite um número entre 0 e 1000.")
            numero = float(input(f"Digite o {i+1}° número: "))

        menor = numero
        maior = numero
        soma = numero
    else:
        numero = float(input(f"Digite o {i+1}° número: "))
        while numero < 0 or numero > 1000:
            print("Valor inválido! Digite um número entre 0 e 1000.")
            numero = float(input(f"Digite o {i+1}° número: "))
            
        soma += numero
        if numero < menor:
            menor = numero
        elif numero > maior:
            maior = numero

print(f"""Maior: {maior}
Menor: {menor}
Soma: {soma}""")
# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-08
# Exercício: Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.



while True:
    populacao_a = float(input("Digite a população do país A: "))
    taxa_a = float(input("Digite a taxa de crescimento do país A: "))
    populacao_b = float(input("Digite a população do país B: "))
    taxa_b = float(input("Digite a taxa de crescimento do país B: "))

    ano = 0

    while populacao_a  < populacao_b:
        populacao_a += populacao_a * taxa_a
        populacao_b += populacao_b * taxa_b
        ano += 1

    print(f"A população de A ultrapassará B em {ano} anos.")
    print("Deseja repetir a operação? (S/N)")
    if input().upper() == "N":
        break
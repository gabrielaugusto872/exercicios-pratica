# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-11
# Exercício: A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

atual = 1

n = int(input("Digite até qual termo você deseja visualizar a série de Fibonacci: "))

if n == 1:
    print("1")
else:
    anterior = 0
    for i in range(n):
        if i < n-1:
            print(atual, end=", ")
            soma = anterior + atual
            anterior = atual
            atual = soma
        else:
            print(atual)
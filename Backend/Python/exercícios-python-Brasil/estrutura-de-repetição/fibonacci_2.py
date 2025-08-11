# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-11
# Exercício: A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.

atual = 1
anterior = 0

while atual <= 500:
    print(atual, end=", ")
    soma = anterior + atual
    anterior = atual
    atual = soma
else:
    print(atual)
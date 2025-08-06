# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-06
# Exercício: Faça um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

letra = input("Digite a letra: ").strip()

if letra.upper() == "F":
    print("F - Feminino")
elif letra.upper() == "M":
    print("M - Masculino")
else:
    print("Sexo Inválido")
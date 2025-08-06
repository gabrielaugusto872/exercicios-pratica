# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-06
# Exercício: Faça um programa que verifique se uma letra digitada é vogal ou consoante.

VOGAL = "AEIOU"

letra = input("Digite a letra: ").strip()

if letra.upper() in VOGAL:
    print(f"A letra {letra} é uma vogal.")
else:
    print(f"A letra {letra} é uma consoante.")
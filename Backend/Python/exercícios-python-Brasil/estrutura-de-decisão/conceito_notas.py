# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-06
# Exercício: Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média.

APROVADO = "ABC"
REPROVADO = "DE"

conceito = ""

nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))

media = (nota_1 + nota_2)/2

if media <= 4.0:
    conceito = "E"
elif media <= 6.0:
    conceito = "D"
elif media <= 7.5:
    conceito = "C"
elif media <= 9.0:
    conceito = "B"
elif media <=10:
    conceito = "A"

print(f"Notas: {nota_1} e {nota_2}")
print(f"Média: {media}")
print(f"Conceito: {conceito}")

if conceito in APROVADO:
    print("APROVADO")
elif conceito in REPROVADO:
    print("REPROVADO")

# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-12
# Exercício: Faça um programa que calcule o número médio de alunos por turma.

soma = 0

turmas = int(input("Digite a quantidade de turmas: "))

for i in range(turmas):
    alunos = int(input(f"Digite a quantidade de alunos na {i+1}° turma: "))
    while alunos > 40:
        print()
        print("As turmas não podem ter mais de 40 alunos!")
        print()
        alunos = int(input(f"Digite a quantidade de alunos na {i+1}° turma novamente: "))
        soma += alunos

media = soma/turmas

print(f"Número médio de alunos por turma: {media:.2f}")
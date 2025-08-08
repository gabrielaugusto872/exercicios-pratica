# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-07
# Exercício: Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#            A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#            A mensagem "Reprovado", se a média for menor do que sete;
#            A mensagem "Aprovado com Distinção", se a média for igual a dez.



media = 0

nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
nota_3 = float(input("Digite a terceira nota: "))

media = (nota_1 + nota_2 + nota_3)/3

if media >= 7:
    print(f"Aprovado com a média de {media}")
elif media == 10:
    print("Aprovado com distinção.")
elif media < 7:
    print(f"Reprovado com a média de {media}")

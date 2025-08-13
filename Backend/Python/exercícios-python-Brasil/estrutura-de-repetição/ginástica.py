# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-13
# Exercício: Competição de ginástica...

nome = input("Atleta: ").strip().title()
while nome !="":

    for i in range(7):
        notas = float(input("Nota: "))
        if i == 0:
            maior = notas
            menor = notas
            soma = notas
        else:
            if notas > maior:
                maior = notas
            elif notas < menor:
                menor = notas
            
            soma += notas
    
    soma -= (maior + menor)
    media = soma / 7

    print()
    print("Resultado final: ")
    print(f"""Atleta: {nome}
Melhor nota: {maior}
Pior nota: {menor}
Média: {media:.2f}""")
    print()

    nome = input("Atleta: ").strip().title()

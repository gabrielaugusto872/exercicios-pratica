# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-13
# Exercício: Correção de Gabarito

VALOR_QUESTOES = 1

maior = -1
menor = 11
soma_notas = 0
alunos = 0
gabarito = ""

print("Insira as respostas do gabarito")
for i in range(0,10):
    gabarito += input(f"{i+1:02}"+" - ").strip().upper()

while True:

    acertos = 0
    erros = 0
    nota = 0

    print()
    print("Digite as alternativas de acordo com as suas respostas")
    for i in range(0,10):
        alternativa = input(f"{i+1:02}"+" - ").strip().upper()
        if alternativa == gabarito[i]:
            acertos += 1
        else:
            erros += 1

    nota = acertos * VALOR_QUESTOES

    if nota > maior:
        maior = nota
    elif nota < menor:
        menor = nota
    
    soma_notas += nota
    alunos += 1

    print(f"Nota = {nota}({acertos} acertos e {erros} erros)")
    
    print("Há mais alunos para correção?(S/N)")
    verificacao = input("").strip().upper()
    if verificacao == "N":
        break

media = soma_notas / alunos

print(f"Total de alunos que utilizaram o sistema: {alunos}")
print(f"Maior nota: {maior}")
print(f"Menor nota: {menor}")
print(f"Média de notas da turma: {media}")

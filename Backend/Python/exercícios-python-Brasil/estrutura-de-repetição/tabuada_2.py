# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-12
# Exercício: Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário

tabuada = int(input("Montar a tabuada de: "))
inicio = int(input("Começar por: "))
fim = int(input("Terminar em: "))

while fim < inicio:
    print("O número final não pode ser maior que o inicial.")
    fim = int(input("Terminar em: "))

print(f"Vou montar a tabuada de {tabuada} começando em {inicio} e terminando em {fim}:")

for i in range(inicio, fim+1):
    conta = tabuada * i
    print(f"{tabuada} X {i} = {conta}")
    
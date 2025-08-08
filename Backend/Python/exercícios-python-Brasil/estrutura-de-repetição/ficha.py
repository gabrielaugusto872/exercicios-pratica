# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-08
# Exercício: Faça um programa que leia e valide as seguintes informações:
#            Nome: maior que 3 caracteres;
#            Idade: entre 0 e 150;
#            Salário: maior que zero;
#            Estado Civil: 's', 'c', 'v', 'd';

ESTADOS_CIVIS = "SCVD"

nome = input("Digite o nome: ")
while len(nome) < 3:
    print("O nome deve ter pelo menos 3 caracteres.")
    nome = input("Digite o nome: ")

idade = int(input("Digite a idade: "))
while idade < 0 or idade > 150:
    print("A idade deve estar entre 0 e 150 anos.")
    idade = int(input("Digite a idade: "))

salario = float(input("Digite o salário: "))
while salario <= 0:
    print("O salário deve ser maior que 0.")
    salario = float(input("Digite o salário: "))


estado_civil = input("Digite o estado civil: ")
while estado_civil.upper() not in ESTADOS_CIVIS:
    print("O estado civil deve ser válido.")
    estado_civil = input("Digite o estado civil: ")

print(f"---- Informações ----")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: {salario}")
print(f"Estado Civil: {estado_civil}")
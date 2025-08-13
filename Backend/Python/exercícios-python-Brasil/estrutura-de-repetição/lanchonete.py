# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-13
# Exercício: Faça um programa que leia o código dos itens pedidos e as quantidades desejadas.

soma = 0
nota = (" LANCHONETE DONA ODETTE ".center(44, "#")) + "\n"
nota += f"{"Código":<10} | {"Quantidade":<15} | {"Preço a pagar":<20}" + "\n"

codigo = int(input("Digite o código do produto: "))
while codigo !=0:
    quantidade = int(input("Digite a quantidade deste produto: "))

    if codigo == 100:
        preço = quantidade * 1.20
        soma += preço
        nota += f"{f"{codigo}":<10} | {f"{quantidade}":<15} | {f"R$ {preço:.2f}":<20}" + "\n"
    elif codigo == 101:
        preço = quantidade * 1.30
        soma += preço
        nota += f"{f"{codigo}":<10} | {f"{quantidade}":<15} | {f"R$ {preço:.2f}":<20}" + "\n"
    elif codigo == 102:
        preço = quantidade * 1.50
        soma += preço
        nota += f"{f"{codigo}":<10} | {f"{quantidade}":<15} | {f"R$ {preço:.2f}":<20}" + "\n"
    elif codigo == 103:
        preço = quantidade * 1.20
        soma += preço
        nota += f"{f"{codigo}":<10} | {f"{quantidade}":<15} | {f"R$ {preço:.2f}":<20}" + "\n"
    elif codigo == 104:
        preço = quantidade * 1.30
        soma += preço
        nota += f"{f"{codigo}":<10} | {f"{quantidade}":<15} | {f"R$ {preço:.2f}":<20}" + "\n"
    elif codigo == 105:
        preço = quantidade * 1.00
        soma += preço
        nota += f"{f"{codigo}":<10} | {f"{quantidade}":<15} | {f"R$ {preço:.2f}":<20}" + "\n"

    codigo = int(input("Digite o código do produto: "))

nota += ("-" * 44) + "\n"
nota += f"Valor total: R$ {soma:.2f}"
print()
print(nota)
print()
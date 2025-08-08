# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-07
# Exercício: Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.


tipo = input("Digite o tipo da carne: ")
quantidade = float(input("Digite a quantidade: "))
pagamento = input("Digite a forma de pagamento: ")

if tipo.strip() == "File Duplo":
    if quantidade <= 5:
        preco_total = quantidade * 4.90
    else:
        preco_total = quantidade * 5.80

if tipo.strip() == "Alcatra":
    if quantidade <= 5:
        preco_total = quantidade * 5.90
    else:
        preco_total = quantidade * 6.80

if tipo.strip() == "Picanha":
    if quantidade <= 5:
        preco_total = quantidade * 6.90
    else:
        preco_total = quantidade * 7.80

valor = preco_total

if pagamento.strip() == "Tabajara":
    valor = preco_total - (preco_total * 0.05)


print("\n" + "Nota Fiscal".center(40, "-"))
print(f"Tipo: {tipo}")
print(f"Quantidade: {quantidade:.2f} Kg")
print(f"Preço total: $ {preco_total:.2f}")
print(f"Tipo de pagamento: {pagamento}")
print(f"Desconto: $ {preco_total - valor:.2f}")
print(f"Valor a pagar: $ {valor:.2f}")
print("-" * 40)
# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-12
# Exercício: O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra.

while True:
    total = 0
    quantidade = 0
    print()
    print("Lojas Tabajara")
    valor = float(input(f"Produto {quantidade+1}: R$ "))
    while valor != 0:
        total += valor
        quantidade += 1
        valor = float(input(f"Produto {quantidade+1}: R$ "))
    
    print(f"Total: R$ {total:.2f}")
    pagamento = float(input("Dinheiro: R$ "))

    troco = pagamento - total

    print(f"Troco: R$ {troco:.2f}")
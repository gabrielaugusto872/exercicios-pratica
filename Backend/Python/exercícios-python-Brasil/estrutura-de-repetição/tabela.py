# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-12
# Exercício: Você foi contratado para desenvolver o programa que monta esta tabela de preços, que conterá os preços de 1 até 50 produtos

print("Lojas Quase Dois - Tabela de preços")

for i in range(50):
    conta = (i+1) * 1.99
    print(f"{i+1} - R$ {conta:.2f}")
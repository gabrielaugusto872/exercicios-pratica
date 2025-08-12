# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-12
# Exercício: Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário

pao = float(input("Digite o preço do pão: "))

print(f"Preço do pão: R$ {pao:.2f}")
print("Panificadora Pão de Ontem - Tabela de preços")

for i in range(50):
    conta = (i+1) * pao
    print(f"{i+1} - R$ {conta:.2f}")
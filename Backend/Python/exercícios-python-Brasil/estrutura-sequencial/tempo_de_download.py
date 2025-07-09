# Autor: Gabriel Augusto dos Santos
# Data: 2025-07-09

tamanho = float(input("Digite o tamanho do arquivo em Mb: "))
velocidade_Mbps = float(input("Digite a velocidade em Mbps: "))

velocidade = velocidade_Mbps / 8

tempo_de_download = tamanho / velocidade
tempo_em_minutos = tempo_de_download / 60
print(f"O tempo de download esperado é de {tempo_em_minutos} minutos.")

# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-06
# Exercício: Faça um programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = input("""Digite a letra de acordo com o turno em que você estuda:
M - Matutino
V - Vespertino
N - noturno
""").strip()

if turno.upper() == "M":
    print("Bom Dia!")
elif turno.upper() == "V":
    print("Boa Tarde!")
elif turno.upper() == "N":
    print("Boa Noite!")
else:
    print("Valor Inválido!")

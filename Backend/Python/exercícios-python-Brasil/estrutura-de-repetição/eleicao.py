# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-12
# Exercício: Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

votos = ""
fulano = 0
beltrano = 0
ciclano = 0
invalidos = 0

eleitores = int(input("Digite o número total de eleitores: "))

for i in range(eleitores):
    print(" ELEIÇÃO DO BAIRRO ".center(30, "#"))
    print("CANDIDATOS:")
    print("A - Fulano")
    print("B - Beltrano")
    print("C - Ciclano")
    print("Digite a letra do candidato em que você deseja votar.")
    votos += input(f"Eleitor N° {i+1}: ").strip().upper()
    print()

for candidatos in votos:
    if candidatos == "A":
        fulano += 1
    elif candidatos == "B":
        beltrano += 1
    elif candidatos == "C":
        ciclano += 1
    else:
        invalidos += 1

print(" ELEIÇÃO DO BAIRRO ".center(30, "#"))
print("RESULTADO:")
print(f"A - Fulano ({fulano} votos)")
print(f"B - Beltrano ({beltrano} votos)")
print(f"C - Ciclano ({ciclano} votos)")
print(f"Votos Inválidos: {invalidos}")
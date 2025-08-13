# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-13
# Exercício: Eleição...

jose = 0
joao = 0
jorge = 0
julio = 0
nulo = 0
brancos = 0
soma = 0

print("ELEIÇÃO PRESIDENCIAL".center(40, "#"))
print("1 - José")
print("2 - João")
print("3 - Jorge")
print("4 - Julio")
print("5 - Voto nulo")
print("6 - Voto em Branco")

votos = int(input("Digite o seu voto: "))
while votos != 0:
    match votos:
        case 1:
            jose += 1
        case 2:
            joao += 1
        case 3:
            jorge += 1
        case 4:
            julio += 1
        case 5:
            nulo +=1
        case 6:
            brancos += 1
        case _:
            print("Voto inválido")
            soma -= 1
    soma += 1

    votos = int(input("Digite o seu voto: "))

porcentagem_nulos = soma / nulo 
porcentagem_brancos = soma / brancos

print(f"José: {jose} votos")
print(f"João: {joao} votos")
print(f"Jorge: {jorge} votos")
print(f"Julio: {julio} votos")
print(f"Nulos: {nulo} votos")
print(f"Em branco: {brancos} votos")
print(f"{porcentagem_nulos}% dos votos nulos foram nulos")
print(f"{porcentagem_brancos}% dos votos foram em branco")
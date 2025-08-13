# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-13
# Exercício: Competição de salto...

nome = input("Digite o nome do atleta: ")

while nome != "":
    maior = -1
    menor = None
    soma = 0
    
    for i in range(5):
        distancias = float(input(f"Digite a {i+1}° distância alcançada por {nome.title()}: "))
        if distancias > maior:
            maior = distancias
        elif menor == None or distancias < menor:
            menor = distancias
        
        soma += distancias
    soma -= (menor + maior)
    media = soma / 3

    print()
    print(f"Melhor salto: {maior:.1f} m")
    print(f"Pior salto: {menor:.1f} m")
    print(f"Média dos demais saltos: {media:.1f} m")
    print()
    print(f"Resultado final:")
    print(f"{nome.title()}: {media:.1f} m")

    print()
    nome = input("Digite o nome do atleta: ")
    
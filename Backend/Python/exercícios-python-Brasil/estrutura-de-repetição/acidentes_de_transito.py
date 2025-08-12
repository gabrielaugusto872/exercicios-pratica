# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-12
# Exercício: Deseja-se saber:
#            Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
#            Qual a média de veículos nas cinco cidades juntas;
#            Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

soma_menor = 0
cidades_pequenas = 0

for i in range(5):
    codigo = int(input(f"Digite o código da {i+1}° cidade: "))
    veiculos = int(input("Digite o número de veículos de passeio: "))
    acidentes = int(input("Digite o número de acidentes com vítimas: "))

    if i == 0:
        maior_codigo = codigo
        menor_codigo = codigo

        maior = acidentes
        menor = acidentes

        soma = veiculos

        if veiculos < 2000:
            cidades_pequenas += 1
            soma_menor += acidentes
    else:
        if acidentes > maior:
            maior_codigo = codigo
            maior = acidentes
        elif acidentes < menor:
            menor_codigo = codigo
            menor = acidentes
        
        soma += veiculos

        if veiculos < 2000:
            cidades_pequenas += 1
            soma_menor += acidentes

media_menor = soma_menor / cidades_pequenas
media = soma / 5
        
print(f"A cidade com o maior índice de acidentes de trânsito possui o código {maior_codigo} e lá houveram {maior} acidentes em 1999.")
print(f"A cidade com o menor índice de acidentes de trânsito possui o código {menor_codigo} e lá houveram {menor} acidentes em 1999.")
print(f"Média de veículos nas cinco cidades: {media}") 
print(f"Média de acidentes nas cidades com menos de 2000 veículos de passeio: {media_menor}")
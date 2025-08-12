# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-12
# Exercício: Academia...

quantidade = 0

while True:
    print()
    print(f" {quantidade+1}° ALUNO ".center(20, "#"))
    codigo = int(input("Digite seu código: "))
    if codigo == 0:
        break
    else:
        altura = float(input("Digite sua altura: "))
        peso = float(input("Digite seu peso: "))

        if quantidade == 0:
            codigo_gordo = codigo
            codigo_magro = codigo
            codigo_alto = codigo
            codigo_baixo = codigo

            gordo = peso
            magro = peso

            alto = altura
            baixo = altura
        else:
            if peso > gordo:
                codigo_gordo = codigo
                gordo = peso
            elif peso < magro:
                codigo_magro = codigo
                magro = peso
            
            if altura > alto:
                codigo_alto = codigo
                alto = altura
            elif altura < baixo:
                codigo_baixo = codigo
                baixo = altura

        quantidade += 1

print(f"O aluno mais gordo possui o código {codigo_gordo} e possui {gordo:.2f} Kg")
print(f"O aluno mais magro possui o código {codigo_magro} e possui {magro:.2f} Kg")
print(f"O aluno mais alto possui o código {codigo_alto} e possui {alto} cm")
print(f"O aluno mais baixo possui o código {codigo_baixo} e possui {baixo} cm")
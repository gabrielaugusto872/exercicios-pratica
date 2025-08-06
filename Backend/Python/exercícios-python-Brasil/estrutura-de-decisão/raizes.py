# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-06
# Exercício: Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.

print("Ax^2 + bx + c")
a = float(input("Digite o valor de A: "))
if a != 0:
    delta = 0

    b = float(input("Digite o valor de B: "))
    c = float(input("Digite o valor de C: "))

    delta = (b ** 2) - (4 * a * c)

    if delta < 0:
        print("A equação não possui raízes reais.")
    elif delta == 0:
        print(f"A raíz dessa equação é: {(-b) / 2*a}")
    else:
        raiz_1 = (-b + (delta ** 0.5)) / 2 * a
        raiz_2 = -b - (delta ** 0.5) / 2 * a
        print(f"As raízes dessa equação são: {raiz_1} e {raiz_2}")
    

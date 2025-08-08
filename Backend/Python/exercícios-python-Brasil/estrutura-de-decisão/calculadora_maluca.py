# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-07
# Exercício: Faça um programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#            par ou ímpar;
#            positivo ou negativo;
#            inteiro ou decimal.

numero_1 = float(input("Digite o primeiro número: "))
numero_2 = float(input("Digite o segundo número: "))
operacao = input("Digite o sinal da operação desejada: ").strip()

if operacao == "+":
    resultado = numero_1 + numero_2
elif operacao == "-":
    resultado = numero_1 - numero_2
elif operacao == "*":
    resultado = numero_1 * numero_2
elif operacao == "/":
    if numero_2 == 0:
        print("Não existe divisão por zero!")
    else:
        resultado = numero_1 / numero_2
else:
    print("Operação inválida!")

if resultado % 2 == 0:
    par_impar = "Par"
else:
    par_impar = "Ímpar"

if resultado == int(resultado):
    inteiro_decimal = "Inteiro"
else:
    inteiro_decimal = "Decimal"

if resultado > 0:
    positivo_negativo = "Positivo"
elif resultado < 0:
    positivo_negativo = "Negativo"
else:
    positivo_negativo = ""

print(f"""{numero_1} {operacao} {numero_2} = {resultado}
{par_impar}
{inteiro_decimal}
{positivo_negativo}""")
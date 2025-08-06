# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-06
# Exercício: Faça um programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

MESES = "1,2,3,4,5,6,7,8,9,10,1"
data = input("Digite uma data (dd/mm/aaaa): ")

#len retorna o comprimento da string
if len(data) == 10 and data[2] == "/" and data[5] == "/":
    dia = int(data[0:2])
    mes = int(data[3:5])
    ano = int(data[6:10])

    if mes > 0 and mes <= 12:
        if mes == 2:
            if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
                if dia > 0 and dia <= 29:
                    print("Data Válida!")
                else:
                    print("Data Inválida!") 
            else:
                if dia > 0 and dia <= 28:
                    print("Data Válida!")
                else:
                    print("Data Inválida!")
        elif mes in [1,3,5,7,8,10,12]:
            if dia > 0 and dia <= 31:
                print("Data Válida!")
            else:
                print("Data Inválida!")
        elif mes in [4,6,9,11]:
            if dia > 0 and dia <= 30:
                print("Data Válida!")
            else:
                print("Data Inválida!")
    else:
        print("Data Inválida!")  
else:
    print("Data Inválida!")

# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-07
# Exercício: Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
#            O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.

contagem = 0
veredito = ""

print("")
print(" QUESTIONÁRIO SUSPEITOS ".center(50, "#"))
print("Digite o nome do suspeito:")
suspeito = input()
print("Telefonou para a vítima?(S/N):")
sim_nao = input().upper()
respostas = f" PISTAS ({suspeito}) ".center(40, "#")
respostas += "\n"
if sim_nao == "S":
    respostas += "Telefonou para a vítima.\n"
    contagem += 1

print("Esteve no local do crime?(S/N):")
sim_nao = input().upper()
if sim_nao == "S":
    respostas += "Esteve no local do crime.\n"
    contagem += 1

print("Mora perto da vítima?(S/N):")
sim_nao = input().upper()
if sim_nao == "S":
    respostas += "Mora perto da vítima.\n"
    contagem += 1

print("Devia para a vítima?(S/N):")
sim_nao = input().upper()
if sim_nao == "S":
    respostas += "Devia para a vítima.\n"
    contagem += 1

print("Já trabalhou com a vítima?(S/N):")
sim_nao = input().upper()
if sim_nao == "S":
    respostas += "Já trabalhou com a vítima,\n"
    contagem += 1

respostas += ("".center(40,"#"))

if contagem == 5:
    veredito = "Assasino!"
elif contagem == 3 or contagem == 4:
    veredito = "Cúmplice!"
elif contagem == 2:
    veredito = "Supeito!"
else:
    veredito = "Inocente!"

print("")
print(respostas)
print("")

print("VEREDITO:")
print(f"O réu {suspeito} é considerado {veredito}")
print("")
# Autor: Gabriel Augusto dos Santos
# Data: 2025-08-08
# Exercício: Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

while True:
    usuario = input("Digite o seu nome de usuário: ").strip()
    senha = input("Digite uma senha: ").strip()

    if senha.lower() == usuario.lower():
        print("Senha e usuário devem ser diferentes entre si.")
    else:
        break
'''Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
mostrando uma mensagem de erro e voltando a pedir as informações.​'''
usuario = input("Digite o nome de usuário: ") 
senha = input("Digite sua senha: ")
while senha == usuario:
    print("SENHA INVÁLIDA SEU ENERGUMENO!!!")
    senha = input("Digite sua senha: ")
    if senha != usuario:
        print("Seja bem-vindo!")
print("Acesso Autorizado")

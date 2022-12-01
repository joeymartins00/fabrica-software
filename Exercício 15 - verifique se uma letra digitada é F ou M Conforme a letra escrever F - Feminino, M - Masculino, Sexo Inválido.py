#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

genero = input("Digite se feminino ou masculino: \n")

if genero == "f" or genero == "F":
    print("Feminino")

if genero =="m" or genero == "M":
    print("Masculino")

if genero != "m" and genero != "M" and genero != "f" and genero != "F":
    print("Sexo Indefinido")

    
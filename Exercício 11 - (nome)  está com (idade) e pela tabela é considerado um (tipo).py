#Faça um algoritmo que o usuário possa digitar o seu nome e a sua idade.
#Utilizando a tabela a baixo, verifique em qual item se enquadra a idade da pessoa e escreva a mensagem:
#(nome)  está com (idade) e pela tabela é considerado um (tipo)

nome = input("Digite o nome: \n")
idade = int(input("Digite a idade: \n"))

if idade <= 2:
    print("{} está com {} e pela idade é considerado Bebê. \n".format(nome,idade))

if idade >= 3 and idade <= 11:
    print("{} está com {} e pela idade é considerado  Criança. \n".format(nome,idade))

if idade >= 12 and idade <= 21:
    print("{} está com {} e pela idade é considerado Jovem. \n".format(nome,idade))

if idade >= 22 and idade <= 64:
        print("{} está com {} e pela idade é considerado Adulto. \n".format(nome, idade))

if idade >= 65 and idade <= 100:
        print("{} está com {} e pela idade é considerado Idoso. \n".format(nome, idade))

if idade >= 101:
        print("{} está com {} e pela idade é considerado Muito Velhinho. \n".format(nome, idade))

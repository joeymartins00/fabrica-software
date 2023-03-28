def multiplosArgs(nome,*args):
    print(nome)
    print(args)

multiplosArgs("Joceyr",32,"Bairro jockey Club")

def multiplosArgs2(nome,*args):
    print(args)
    print(nome,"mora na",args[2])

multiplosArgs2("João Leandro",17,6799999-9999,"Rua Tal,22")

def argumentos(nome, idade, estado="Solteiro"):
    print(f"{nome} tem {idade}, estado civil {estado}")

argumentos("João Leandro",17, "Casado")

def variosargs(valor, **kwargs):
    print(valor)
    print(kwargs)

variosargs(1000,nome="Joceyr",fone="3326-5310",endereco="Rua Rio Claro, 55, casa 48, bairro Jardim Veraneio")


def variosargumentos(valor,**kwargs):
    print(valor)
    print(kwargs)
    if kwargs["nome"] == "":
        print("O usuário deve informar um nome!")

variosargumentos(1000, nome="", fone="9985-3058")
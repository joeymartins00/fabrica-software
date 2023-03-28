"""1- Classe Pessoa: Crie uma classe que modele uma pessoa. Esta classe deve possuir os seguintes atributos:
Nome;
Idade;
Endereço;

A classe deve ter os seguintes métodos:
Mostrar nome;
Alterar idade;
Imprimir endereço;"""

#USANDO PRINT

class Pessoa:
    def __init__(self,nome,idade,endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def get_nome(self):
        print(f"Nome: {self.nome}")
        
    def get_idade(self):
        print(f"Nome: {self.idade}")

    def get_endereco(self):
        print(f"Nome: {self.endereco}")

    def set_idade(self,nova_idade):
        self.idade = nova_idade

pessoa1 = Pessoa("Joceyr",32,"Jockey Club")
print(pessoa1.get_nome())
pessoa1.get_nome()
pessoa1.set_idade(17)
print(pessoa1.idade)

'''#USANDO RETURN

class People:
    def __init__(self,nome,idade,endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def get_nome(self):
        return self.nome
 
    def get_idade(self):
        return self.idade
    
    def get_endereco(self):
        return self.endereco
    
    def set_idade(self,nova_idade):
        return nova_idade
       
    

pessoa2 = People("Thiago",32,"Jockey Club")

print(pessoa2.get_nome())

pessoa2.set_idade(17)
people = pessoa2.set_idade()
print(pessoa2.get_idade())'''






class Pessoa:
    def __init__(self,nome,idade=0):
        self.nome = nome
        self.idade = idade
    
    def set_idade(self,idade):
        self.idade = idade

    def get_info(self):
        print(f"{self.nome} tem {self.idade} anos.")

if __name__ == "__main__":
    pes = Pessoa("Naldo Benny")
    print(pes.nome)
    print(pes.idade)

    pes.set_idade(44)
    print(pes.nome)
    print(pes.idade)
    
    pes.get_info()

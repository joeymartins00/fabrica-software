class People:
    def __init__(self,nome,idade):
        self.__nome = nome
        self.idade = idade


    def get_nome(self):
        return self.__nome


    def set_nome(self,name):
        self.__nome = name
        
"""pes1 = People("Luiz", 20)
print(pes1.nome)
pes1.nome = "Thays"
pes1.idade = 28
print(f"Agora a PES vale {pes1.nome} e idade é {pes1.idade}")"""

pes1 = People("Luiz", 20)
pes1.set_nome("Thays Martines")
print(pes1.get_nome())

pes1.idade = 28
print(pes1.idade)
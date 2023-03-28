class Cachorro:
    def __init__(self,nome,raca,cor,idade,porte):
        self.nome = nome
        self.raca = raca
        self.cor = cor
        self.idade = idade
        self.porte = porte

    def comer(self):
        print("Estou com fome!")

    def latir(self):
        print("Au Au")

    def dormir(self):
        print("Ronc Ronc")

    def agua(self):
        print("Estou com sede!")

    def correr(self):
        print("Yuuupi!")

    def brincar(self):
        print("Quero minha bolinha1")

#Get(Buscando valor)

    def get_idade(self):
        return self.idade
    
    def get_porte(self):
        return self.porte
    
#Set(Alterando valor)

    def set_idade(self,nova_idade):
        self.idade = nova_idade


sofia = Cachorro("Sofia", "Labrador","Preta",32,12,"Grande")
sofia.latir()
sofia.dormir()
sofia.comer()


yuji = Cachorro("Yuji","Lhasa Apso","Branco e Marrom","10","1,5","Pequeno")
yuji.agua()
yuji.correr()
yuji.brincar()

print(50*"*")

class Morcego:
    def __init__(self,tipo,apetite):
        self.tipo = tipo
        self.apetite = apetite

    def voar(self):
        print("Estou nas nuvens!")

    def matar(self):
        print("Vou chupar um sanguinho, só de boa!")

draculinha = Morcego ("Sanguinário","Fome de sangue")
draculinha.voar()
draculinha.matar()

print(50*"*")


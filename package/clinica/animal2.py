class Animal:
    def __init__(self,name,color):
        self.name = name
        self.color = color

    def mover(self):
        print(f"{self.name} andou.")


a1 = Animal("Bilú","Caramelo")
a1.mover()

class Gato(Animal):
    def __init__(self,name,color,pedigree):
        super().__init__(name,color)
        self.pedigree = pedigree

    def miar(self):
        print(f"{self.name} miou.")


class Cachorro(Animal):
    def __init__(self,name,color,raca):
        super().__init__(name,color)
        self.raca = raca

    def latir(self):
        print(f"{self.name} latiu.")
    

class Coelho(Animal):
    def __init__(self,name,color,olhos):
        super().__init__(name,color)
        self.olhos = olhos

    def reproduzir(self):
        print(f"{self.name} teve 12 filhotinhos.")


class Peixe(Animal):
    def __init__(self,name,color,peso):
        super().__init__(name,color)
        self.peso = peso

    def mover(self):
        print(f"{self.name} nadou.")


if __name__ == "__main__":
    a1 = Animal("Bilú","Caramelo")
    a1.mover()


    p1 = Peixe("Pintado","Cinza e Preto",10)
    p1.mover()
    print(p1.peso)


    p1 = Gato("Garfield Johnnes","Laranja","Siamês")
    p1.miar()
    print(p1.pedigree)

    p1 = Cachorro("Sophia","Preta","Labrador")
    p1.latir()
    print(p1.raca)

    p1 = Coelho("Pernalonga","Cinza","Azuis")
    p1.reproduzir()
    print(p1.olhos)
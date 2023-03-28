class Animal:
    def __init__(self,name,color):
        self.name = name
        self.color = color

    def mover(self):
        print(f"{self.name} andou.")


a1 = Animal("Bilú","Caramelo")
a1.mover()

class Gato(Animal):
    pass
    def miar(self):
        print(f"{self.name} miou.")


class Cachorro(Animal):
    pass
    def latir(self):
        print(f"{self.name} latiu.")
    

class Coelho(Animal):
    pass
    def reproduzir(self):
        print(f"{self.name} teve 12 filhotinhos.")


g1 = Gato("Garfield", "Laranjado")
g1.miar()

c1 = Cachorro("Sophia","Preta")
c1.latir()

co = Coelho("Pernalonga","Cinza")
co.reproduzir()


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


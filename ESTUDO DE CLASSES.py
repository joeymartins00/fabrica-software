'''ESTUDO DE CLASSES'''

#Exemplo 1


class Estudante:
    def __init__(self, nome, idade, nota): # __init__ é um método construtor que mostra que você está iniciando uma função. // #SELF significa é está atribuindo valores dentro dela mesma.
        self.nome = nome
        self.idade = idade
        self.nota = nota
    
    def mostrar_nome(self,):
        return self.nome
    
#GET OU GETTER (É quando você busca o nome de um objeto)

p1 = Estudante("Wanderley", 32, 88)
e2 = Estudante("Thiago", 28, 85)
estud = Estudante("João", 17, 75)

print(p1.mostrar_nome())
print(e2.mostrar_nome())
print(estud.mostrar_nome())

#SETAR UM OBJETO (É quando você muda o nome de um objeto)

estud.nome = "Lucas"
print(estud.mostrar_nome())

#Exemplo 2

class Retangulo:
    def __init__(self,lado1, lado2):
        self.l1 = lado1
        self.l2 = lado2
        self.area = 0

    def get_lado1(self):
        return self.l1
    
    def get_lado2(self):
        return self.l2
    
    def get_area(self):
        return self.l1 * self.l2

r1 = Retangulo(10,15)
area = r1.get_area()
print(f"A área do retangulo é: {area}")


#TENTATIVA DE RESOLUÇÃO:

class Quadrado:
    def __init__(self, x, y):
        self.ladoX = x
        self.ladoY = y
        self.areaT = 0

    def get_X(self):
        return self.ladoX
    
    def get_Y(self):
        return self.ladoY

    def get_areaT(self):
        return self.ladoX * self.ladoY

aQ = Quadrado(50,25)
areaQuadrado = aQ.get_areaT()
print(f"A área do quadrado é {areaQuadrado}")
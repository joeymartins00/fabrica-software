'''1 - Classe Filme: Crie uma super classe que modele um Filme. Esta classe deve possuir os seguintes atributos:
Nome;
Duração;
Método:
Play(): deve exibir que foi dado play no filme;
Subclasses:
Defina as subclasses de Filme, exemplo Ação, Drama e Suspense. 
Após a criação das subclasses você deve criar novos métodos específicos a cada subclasse, ex: explodir() em Ação.

'''
class Filme:
    def __init__(self,nome,duracao):
        self.__nome = nome
        self.duracao = duracao

    def play(self):
        print(f"Foi dado play no filme {self.nome}, para assistir comendo pipoca.")

class Terror(Filme):
    def __init__(self,nome,duracao,medo):
        super().__init__(nome,duracao)
        self.medo = medo

    def play(self):
        print(f"Foi dado play no filme {self.nome} para assistir {self.medo} Porém ficaram com raiva porque o filme era muito longo, tinha APENAS {self.duracao} de duração!!!")

class Drama(Filme):
    def __init__(self,nome,duracao,emocao):
        super().__init__(nome,duracao)
        self.emocao = emocao

    def drama(self):
        print(f"Comecei a assistir o filme {self.nome} achando que não ia dar nada, mas quando vi estava muito {self.emocao}")

    



film1 = Filme("O VENTO LEVOU",180)


print(film1.__nome)
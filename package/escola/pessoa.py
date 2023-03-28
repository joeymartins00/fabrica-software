'''2 - Classe Pessoa: Crie uma super classe que modele uma Pessoa. Esta classe deve possuir os seguintes atributos:
Matricula; Nome; Idade;  
Subclasses:
Defina as subclasses de Pessoa serão Aluno e Professor, estas devem conter além dos atributos herdados de Pessoa seus atributos identificadores, ex: Classe Aluno (NOTAS; MEDIA). 
Classe Professor (Formacao, Disciplina, Carga Horária e Salario)
Você deve criar métodos específicos para cada subclasse, ex: calcular_media, estudar, lecionar.'''


class Pessoa:
    def __init__(self,nome,idade,matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade, matricula)
        self.notas = []
        self.media = 0.0

    def get_media(self):
        for i in range(1,5):
            self.notas.append(float(input(f'nota {i}: ')))
        self.media = sum(self.notas)/4

        print(f"A média final do aluno {self.nome} é {self.media}.")

    def estudar(self):
        print(f"O aluno com a matrícula de número {self.matricula} e por nome {self.nome} estudou a disciplina de orientação a objetos até ficar craque!")
    
    
class Professor(Pessoa):
    def __init__(self, nome, idade, matricula,formacao,disciplina,carga_horaria,salario):
        super().__init__(nome, idade, matricula)
        self.formacao = formacao
        self.disciplina = disciplina
        self.carga_horaria = carga_horaria
        self.salario = salario

    def lecionar(self):
        print(f"O professor {self.nome} lecionou a disciplina {self.disciplina} durante {self.carga_horaria} horas diárias por 22 dias para receber o salário de {self.salario} pois o valor de sua hora é R$ 8,00.")



a1 = Aluno("Joceyr",32,6071166)
a1.get_media()
    




'''self.notas = []
for i in range(1,5):
    self.notas.append(float(input(f'nota {i}')))
self.media=sum(self.notas)/4'''
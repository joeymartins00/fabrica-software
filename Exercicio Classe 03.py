'''3 - Classe Aluno: Crie uma classe que modele um aluno. Esta classe deve possuir os seguintes atributos:
Nome;
RA;
Nota 1, nota 2, nota 3, nota 4;
A classe deve ter o seguintes método:
Mostrar_situacao: (APROVADO / EXAME / REPROVADO). Considere que, nesse caso, 
a média final é calculada pela média aritmética simples de todas as notas e que o aluno é aprovado somente se obtiver média maior ou igual a sete. 
Exame entre 5 e 6.9. Reprovado abaixo de 5
A situação será retornada a partir das notas obtidas pelo aluno.'''

class Aluno:
    def __init__(self,nome,ra,nota1,nota2,nota3,nota4):
        self.nome = nome
        self.ra = ra
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4
        
    def get_mostrar_situacao(self):
        media_final = (self.nota1+self.nota2+self.nota3+self.nota4)/4
        if media_final >= 7:
            print("Aluno aprovado.")
        elif media_final > 5 and media_final < 7:
            print("Aluno deverá passar por exame final.")
        else:
            print("Aluno reprovado.")


media_aluno = Aluno("Luquinhas", "0242424", 10,10,10,5)
media_aluno.get_mostrar_situacao()

        
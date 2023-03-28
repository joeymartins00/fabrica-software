'''2 - Classe Livro: Crie uma classe que modele um Livro. Esta classe deve possuir os seguintes atributos:
Nome
Autor
Editora
Páginas
A classe deve ter o seguintes métodos:
Alterar_editora()
Listar_qtde_paginas()'''

"""class Livro:
    def __init__(self,nome,autor,editora,paginas):
        self.nome = nome
        self.autor = autor 
        self.editora = editora 
        self.paginas = paginas 

    def get_editora(self):
        return self.editora

    def get_paginas(self):
        return self.paginas

    def set_paginas(self, qtd_paginas):
        self.paginas = qtd_paginas
        return self.paginas

livrinho = Livro("Ponto de Impacto", "Dan Brown", "Fridenswalden", "400")
print(livrinho.get_editora())

print(livrinho.set_paginas("502"))"""

class Livro:
    def __init__(self,nome,autor,editora,paginas):
        self.nome = nome
        self.autor = autor 
        self.editora = editora 
        self.paginas = paginas 

    def get_editora(self):
        print(self.editora)

    def get_paginas(self):
        print(self.paginas)

    def set_paginas(self, qtd_paginas):
        self.paginas = qtd_paginas
        return self.paginas

livrasso = Livro("As relíquias da morte","J.K Rowling", "Sampa Crew", "20")
livrasso.get_editora()
    
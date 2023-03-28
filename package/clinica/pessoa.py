class Pessoa:
    def __init__(self,nome,telefone):
        self.nome = nome
        self.telefone = telefone

    def falar(self):
        print(f"{self.nome} falou!")
    
p1 = Pessoa("Joceyr",6799675-7550)
p1.falar()


class Veterinario(Pessoa):
    pass

class Cliente(Pessoa):
    pass


cli = Cliente("Paula Itokagi", 6799105-6712)
cli.falar()


vet = Veterinario("Joeder Júnior", 6799221-5681)
vet.falar()


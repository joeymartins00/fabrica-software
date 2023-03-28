from person import Pessoa
from contador import Contador

cont = Contador()
lista = []

while True:
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    pessoa = Pessoa(nome,idade)
    lista.append(pessoa)
    cont.increment()

    op = input("Deseja continuar S/N ?").upper()
    if op == "N":
        break

for pes in lista:
    print(pes.nome, pes.idade)
print(cont.get_status())

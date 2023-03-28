'''4 - Classe Conta: Um banco mantém contas de clientes armazenando o número da conta, o nome do cliente e o saldo atual da conta. 
Crie uma classe que modele um Conta-Corrente.
Nome;
CPF;
Numero;
Saldo;
A classe deve ter o seguintes métodos:
Depositar()
Sacar()  -  OBS: somente enquanto a conta possuir saldo positivo
Imprimir saldo()'''

class Conta:
    def __init__(self,nome,cpf,numero,saldo):
        self.nome = nome
        self.cpf = cpf
        self.numero = numero
        self.saldo = saldo

    def get_depositar(self,adicionar_dinheiro):
        self.saldo += adicionar_dinheiro
        return self.saldo
        
    def get_sacar(self,sacar):
        if self.saldo > 0:
            if self.saldo - sacar >= 0:
                self.saldo -= sacar
            else:
                print("Saldo insuficiente Boy!")
        return self.saldo

    def get_imprimir_saldo(self):
        return self.saldo
    
contacorrente = Conta("Lucas Barbosa","024002402424","0240024",240.24)
print(contacorrente.get_depositar(50))
contacorrente.get_sacar(float(input("digite o valor a ser sacado: ")))
print(contacorrente.get_imprimir_saldo())

'''3 – Crie uma função que imprima a quantidade de dígitos de um determinado número inteiro informado.'''
def qtdDigitos(numero):
    return len(str(numero))
    
def exibeDigitos():
    numero = int(input('Digite um número inteiro: '))
    print(qtdDigitos(numero), 'digitos')
    
while True:
    exibeDigitos()
    break
'''1 - Crie uma função que necessite de três argumentos, e que imprima o produto desses três argumentos.'''

def leilao(boi, cavalo, ovelha):
    print(f'Eu comprei um boi {boi} no leilão, e com a venda do meu cavalo {cavalo}, ainda me sobrou R$20.000 pra comprar minha ovelha {ovelha}.')
    
leilao("Angus", "Alazão","Egípcia")

def matematica(x,y,z):
    conta = x+(y*z)
    return conta
    
resultado = matematica(2,20,5)
print(f'O resultado da conta é {resultado}')
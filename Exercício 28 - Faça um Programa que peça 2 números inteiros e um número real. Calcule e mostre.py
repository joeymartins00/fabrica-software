#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.

n1 = int(input('1o Número inteiro: '))
n2 = int(input('2o Número inteiro: '))
n3 = float(input('Número real: '))

print ('Soma:', ((2*n1) * (n2/2)))
print ('Produto:', (3 * n1) + n3)
print ('Cubo:', n3**3)
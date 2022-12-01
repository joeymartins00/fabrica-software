#Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

a = float(input('Primeiro lado: '))
b = float(input('Segundo lado: '))
c = float(input('Terceiro lado: '))

if (a + b < c) or (a + c < b) or (b + c < a):
    print('Nao é um triangulo')

elif (a == b) and (a == c):
    print('Equilatero')

elif (a == b) or (a == c) or (b == c):
    print('Isósceles')

else:
    print('Escaleno')

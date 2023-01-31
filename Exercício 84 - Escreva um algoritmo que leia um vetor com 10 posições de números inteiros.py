'''Escreva um algoritmo que leia um vetor com 10 posições de números inteiros. Em seguida receba um novo valor do usuário e verifique se este valor se encontra no vetor.​'''

encontrado = 0
numeros = []
for c in range(3):
    numeros.append(int(input(f"Digite o número {c+1}: ")))
num = int(input('Número para verificar: '))
for c in range(len(numeros)):
    if num == numeros[c]:
        encontrado = 1
        print("Encontrou!")
    else:
        print("Não encontrou!")
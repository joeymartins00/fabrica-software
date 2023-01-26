'''Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.​'''
pares = 0
impares = 0
for i in range(10):
    if int(input("Digite um número inteiro: ")) %2 == 0:
        pares += 1
    else:
        impares += 1
print(f'Números pares: {pares}\nNúmeros ímpares: {impares}')
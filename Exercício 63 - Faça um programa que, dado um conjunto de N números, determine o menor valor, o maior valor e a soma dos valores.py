'''Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.'''
num = int(input("Digite um número: "))
soma = 0
maior = num
menor = num
while num != -999:
    soma = soma+num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    num = int(input("Digite um número: "))

print(f"A Soma dos valores é {soma}\nO maior número é {maior}\nO menor número é {menor}")



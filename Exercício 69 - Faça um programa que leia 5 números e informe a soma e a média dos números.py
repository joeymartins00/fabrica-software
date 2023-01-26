'''Faça um programa que leia 5 números e informe a soma e a média dos números.​​'''
soma = 0
for c in range(0,5):
    num = float(input("Digite um número: "))
    soma = soma + num

print(f'A soma dos número foi {soma}\nA média dos número foi{soma/5}')
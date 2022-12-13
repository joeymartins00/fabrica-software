#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:


#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

sexo = int(input('Digite seu sexo: (1)Para homem (2)Para mulher: '))

if sexo == 1:
    altura_H = float(input('Digite sua altura: '))
    pesoideal_H = (72.7 * altura_H) - 58
    print(f'Seu peso ideal é {pesoideal_H:.2f} quilos')
    
elif sexo == 2:
    altura_M = float(input('Digite sua altura: '))
    pesoideal_M = (62.1 * altura_M) - 44.7
    print(f'Seu peso ideal é {pesoideal_M:.1f} quilos')

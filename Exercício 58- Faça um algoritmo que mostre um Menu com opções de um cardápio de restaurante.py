'''Faça um algoritmo que mostre um Menu com opções de um cardápio de restaurante para uma pessoa (Coloque no mínimo 5 opções e máximo 10 opções de cardápio. 
Ex: Bife acebolado R$15,00; Lasanha R$25,00).​

A pessoa vai escolher o prato desejado e após escolher o prato, o algoritmo deverá fazer a seguinte pergunta ao usuário, 
“Aceita pagar a gorjeta do garçom 10% sobre o valor do prato”. 
Se o usuário aceitar, mostrar o valor final (valor do prato + 10%), caso contrário, mostrar o valor final (somente o valor do prato).​'''

print('*'*25,'MENU','*'*25,'\n')
print('\n 1- LASANHA À BOLONHESA                     | R$32,00 | 500Gr\n 2- PICANHA NA CHAPA ACEBOLADA              | R$58,00 | 500Gr\n 3- BIFE DE CHORIZO C/ PURÊ DE MANDIOQUINHA | R$35,00 | 300Gr\n 4- MAMINHA NA MANTEIGA C/ ALHO NEGRO       | R$62,00 | 500Gr\n 5- MOQUECA DE JACARÉ À URUCUM              | R$75,00 | 500Gr\n\n')
print('*'*56)
preco = 0
escolher = int(input('Escolha a opção desejada: (1) (2) (3) (4) (5)? '))
if escolher == 1:
    preco = 32.00
if escolher == 2:
    preco = 58.00
if escolher == 3:
    preco = 35.00
if escolher == 4:
    preco = 62.00
if escolher == 5:
    preco = 75.00

pergunta = input('Aceita pagar a gorjeta do garçom 10% sobre o valor do prato? S/N?').upper()
if pergunta == "S":
    preco += preco*0.10
print("O valor total a pagar é R$",preco)
print("VOLTE SEMPRE!")
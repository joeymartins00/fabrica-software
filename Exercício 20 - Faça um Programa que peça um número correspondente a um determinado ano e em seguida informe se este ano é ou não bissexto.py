#Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.
#Uma das duas condições a seguir deve ser verdadeira:
#Condição 1: Ser múltiplo de 4 e não ser múltiplo de 100
#Condição 2: Ser múltiplo de 400 (se for múltiplo de 400 automaticamente é de 4)

#Logo, temos o código:
ano = int(input('Ano: '))

if (ano%4==0 and ano%100!=0) or (ano%400==0):
    print('Bissexto')
else:
    print('Não é bissexto')
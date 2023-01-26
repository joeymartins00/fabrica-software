'''O programa de fidelidade de uma determinada livraria premia seus clientes de acordo com o número de livros comprados a cada bimestre.
Os pontos são atribuídos da seguinte forma:​

•Se um cliente comprar 0 livros, ele ganhará 0 pontos.​
•Se um cliente comprar um livro, ele ganhará 5 pontos.​
•Se um cliente comprar dois livros, ele ganhará 15 pontos.​
•Se um cliente comprar 3 livros, ele ganhará 30 pontos.​
•Se um cliente comprar 4 ou mais livros, ele ganhará 60 pontos.​
Lista de brindes:​

De 20 à 30 pontos o cliente poderá escolher entre: Uma EcoBag OU Caneta personalizada​
De 35-60 pontos o cliente poderá escolher entre: Um livro (com valor máximo de R$30,00) OU Luminária de cabeceira.​
Acima de 65 o cliente poderá escolher entre: 2 livros (com valor máximo de R$100,00) OU Powerbank.
​'''

'''
pontos = 0

for i in range(2):
    qtdLivros = int(input("Digite a quantidade de livros comprados: "))
    
    if qtdLivros == 0:
        pontos = pontos + 0
    if qtdLivros == 1:
        pontos = 5
    if qtdLivros == 2:
        pontos = 15'''

pontos = 0
for contador in range(0,4): # lê de 0 (condição inicial) até 3 (4-1) ##os valores 0 até 4 simboliza o número de bimestre, que são 4.
    quantidadeCompra = int(input("Digite a quantidade de livros que deseja comprar: "))
    if quantidadeCompra == 1:
        pontos += 5
    if quantidadeCompra == 2:
        pontos += 15
    if quantidadeCompra == 3:
        pontos += 30
    if quantidadeCompra >= 4:
        pontos += 60

premio = 0
if pontos >= 20 and pontos <= 30:
    premio = int(input("(1) Escolha uma  Ecobag ou (2) uma Caneta personalizada."))
    if premio == 1:
        premio = 'Ecobag'
    else:
        premio = 'Caneta Personalizada'
            
if pontos >= 35 and pontos <= 60:
    premio = int(input("(1) Escolha um livro no valor máximo de R$ 30,00 ou (2) uma Luminária de cabeceira."))    
    if premio == 1:
        premio = 'Livro de no máximo R#30,00'
    else:
        premio = 'Luminária de cabeceira'
if pontos >=65:
    premio = int(input("(1) Escolha 2 livros com o valor máximo de R$100,00 ou (2) um Powerbank."))    
    if premio == 1:
        premio = '2 livros com o valor máximo de R$100,00'
    else:
        premio = 'Powerbank'

print('Nossa! Você é muito sortudo mesmo conseguiu o seu tão sonhado premio:',premio)
    


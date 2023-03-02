'''5 – Escreva um programa com uma função chamada somaImposto. 
A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e 
custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas. 
Por fim deve retornar o novo valor para o usuário considerando o percentual do imposto.'''

def somaImposto(taxaImposto,custo,lucro):
    return custo+(custo*taxaImposto)+(custo*lucro)
print(somaImposto(float(input("Digite a taxa de imposto: "))/100, 
                  float(input("Digite o custo do produto: ")), 
                  float(input("Digite o lucro do produto: "))/100))
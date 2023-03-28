'''5 – Escreva um programa com uma função chamada somaImposto. 
A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo,
que é o custo de um item antes do imposto. 
A função “altera” o valor de custo para incluir o imposto sobre vendas. 
Por fim deve retornar o novo valor para o usuário considerando o percentual do imposto.'''

def somaImposto(custo,taxaImposto):
    custo += taxaImposto
    return custo
    
valorFinal = somaImposto(100,10)
print(f'O valor final é R${valorFinal:.2f} pois a porcentagem da taxa de imposto aplicada é de 10%.')
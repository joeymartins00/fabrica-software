'''12 - Crie uma função que receba uma lista como argumento, 
os valores da lista devem ser numéricos, 
por fim retorne a média desses valores.'''
numeros=[]
numeros.append(2)
numeros.append(8)
numeros.append(6)
numeros.append(7)
print(numeros)


def mediaNumeros(numeros):
    contador=0
    soma=0
    for adicionar in numeros:
        contador+=1
        soma += adicionar

    return(soma/contador)

resultado = mediaNumeros(numeros)
print("O resultado é:" ,resultado)
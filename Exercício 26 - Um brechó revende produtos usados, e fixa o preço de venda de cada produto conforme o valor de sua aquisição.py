# Um brechó revende produtos usados, e fixa o preço de venda de cada produto conforme o valor de sua aquisição:
# Se o preço de aquisição de um produto é menor que R$ 50,00, ele deve ser vendido por um preço 45% maior, caso contrário o lucro será de 30%.
# Sabendo disso, faça um algoritmo que leia o valor de aquisição de um produto e mostre o seu valor de venda.

valor_aquisicao = float(input("Informe o valor do produto: "))
print("Informe o valor do produto: \n", valor_aquisicao)

if valor_aquisicao < 50:
    valor_venda = valor_aquisicao + (valor_aquisicao * 0.45)
    print(f'O valor de venda é de {valor_venda}')

else:
    valor_aquisicao >= 50
    valor_venda = valor_aquisicao + (valor_aquisicao * 0.30)
    print(f'O valor de venda é de {valor_venda}')
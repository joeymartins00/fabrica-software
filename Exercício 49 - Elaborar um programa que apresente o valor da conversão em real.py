#Elaborar um programa que apresente o valor da conversão em real (R$) de um valor lido em dólar (US$). 
# O programa deve solicitar o valor da cotação do dólar.
print("*************COTAÇÃO DO DÓLAR HOJE*************")
cotacaoDolar = float(input("Qual a cotação do Dólar hoje?: "))
print(cotacaoDolar)
dolarAmericano = float(input("Quantos Dólares você possui?: "))
print(dolarAmericano)
realBrasileiro = dolarAmericano/cotacaoDolar
print(f"{dolarAmericano:.4} Dólares equivalem a R${realBrasileiro:.4}")
print("****************FIM DA OPERAÇÃO****************")
#Utilizei a formatação de 4 casas decimais para aparecer os valores necessários numa operação de conversão de moedas internacionais.

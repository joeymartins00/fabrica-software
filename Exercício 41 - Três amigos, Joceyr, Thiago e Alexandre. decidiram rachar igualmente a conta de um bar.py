#Três amigos, Joceyr, Thiago e Alexandre. decidiram rachar igualmente a conta de um bar. 
# Faça um algoritmo para ler o valor total da conta e imprimir quanto cada um deve pagar, mas faça com que Joceyr e Thiago não paguem centavos. 
# Ex: uma conta de R$101,53 resulta em R$33,00 para Joceyr, R$33,00 para Thiago e R$35,53 para Alexandre.

valor_conta = float(input('informe o valor da conta a se pagar:. '))

# verificando se o valor da conta é válido
if valor_conta < 0.00:
    valor_conta = 0.00

# calculando quanto cada um terá que pagar
valor_terco = valor_conta/3

valor_joceyr    = valor_terco - (valor_terco - int(valor_terco))
print(valor_joceyr)
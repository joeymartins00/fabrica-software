'''Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela. Os juros e a quantidade de parcelas seguem a tabela abaixo:​

Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida​
1       0​
3       10​
6       15​
9       20​
12      25​

​

Exemplo de saída do programa:​

Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela​
R$ 1.000,00     0               1                       R$  1.000,00​
R$ 1.100,00     100             3                       R$    366,00​
R$ 1.150,00     150             6                       R$    191,67​

​'''
valorDivida = float(input("Digite o valor da divida: "))
print("\n")
print("*"*43,"TABELA GERAL","*"*43,"\n")
print(          "Valor da Dívida  | Valor dos Juros | Quantidade de Parcelas | Valor da Parcela"          )
print(f'R$ {valorDivida*1:.2f}       |               0 |                      1 | R$ {valorDivida:.2f}')
print(f'R$ {valorDivida*1.10:.2f}       |              10 |                      3 | R$ {valorDivida*1.10/3:.2f}')
print(f'R$ {valorDivida*1.15:.2f}       |              15 |                      6 | R$ {valorDivida*1.15/6:.2f}')
print(f'R$ {valorDivida*1.20:.2f}       |              20 |                      9 | R$ {valorDivida*1.20/9:.2f}')
print(f'R$ {valorDivida*1.25:.2f}       |              25 |                     12 | R$ {valorDivida*1.25/21:.2f}\n')
print("*"*101,"\n")
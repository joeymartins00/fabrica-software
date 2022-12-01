#Um funcionário recebe um salário fixo mais 4% de comissão sobre vendas.
# Faça um algoritmo que receba o salário fixo de um funcionário e o valor de suas vendas, calcule e mostre o valor da comissão e o salário final do funcionário.

salario_fixo = float(input("Digite o salário do funcionário: \n"))
comissao = float(input("Digite a porcentagem de comissão por venda realizada: \n"))
venda = float(input("Digite o valor vendido: \n"))

salario_final = salario_fixo+(comissao*venda)
print(salario_final)
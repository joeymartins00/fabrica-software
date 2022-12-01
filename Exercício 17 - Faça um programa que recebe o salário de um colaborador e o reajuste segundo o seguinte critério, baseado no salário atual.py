#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhes contrataram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.

salario = float(input("Digite o salário do colaborador: \n"))
aumento20 = salario*0.20
aumento15 = salario*0.15
aumento10 = salario*0.10
aumento5 = salario*0.05

if salario <= 280 :
    salario_atual = salario+(salario * 0.2)
    print(f"O aumento do salário foi de 20%, seu novo salário é de {salario_atual}")

elif salario > 208 and salario <= 700 :
     salario_atual = salario+(salario*0.15)
     print(f"O aumento do salário foi de 15%, seu novo salário é de {salario_atual}")

elif salario > 700 and salario <=1500 :
     salario_atual = salario+(salario * 0.10)
     print(f"O aumento do salário foi de 10%, seu novo salário é de {salario_atual}")

elif salario > 1500 :
     salario_atual = salario+(salario * 0.05)
     print(f"O aumento do salário foi de 5%, seu novo salário é de {salario_atual}")


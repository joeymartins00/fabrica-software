#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
#que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
# mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

# Salário Bruto: (5 * 220)        : R$ 1100,00
#        (-) IR (5%)                     : R$   55,00
#        (-) INSS ( 10%)             : R$  110,00
#        (-) SINDICATO (3%)          : R$ 33,00
#         FGTS (11%)                  : R$  121,00
#        Total de descontos        : R$  165,00
#        Salário Liquido              : R$  90,00

valor_hora = float(input("Digite o valor da hora: "))
qtd_hora = float(input("Digite a quantidade de horas trabalhadas: "))

salarioBruto = valor_hora*qtd_hora

if salarioBruto <= 900:
    sindicato = salarioBruto*0.03
    inss = salarioBruto*0.1
    fgts = salarioBruto*0.11
    salarioLiquido = salarioBruto - sindicato - inss

    print(f"Valor do Salário Bruto R$ {salarioBruto:.2f}")
    print(f"Valor do sindicato     R$ {sindicato:.2f}")
    print(f"Valor do INSS          R$ {inss:.2f}\n")
    print(f"O valor do salário líquido é R$ {salarioLiquido:.2f}")
    print(f"O valor do FGTS depositado em conta é: R$ {fgts:.2f}")

elif salarioBruto > 900 and salarioBruto <=1500:
    ir = salarioBruto * 0.05
    sindicato = salarioBruto*0.03
    inss = salarioBruto*0.10
    fgts = salarioBruto*0.11
    salarioLiquido = salarioBruto - sindicato - inss -ir
    print(f"Valor do Salário Bruto R$ {salarioBruto:.2f}")
    print(f"Valor do Sindicato     R$ {sindicato:.2f}")
    print(f"Valor do IR            R$ {ir:.2f}")
    print(f"Valor do INSS          R$ {inss:.2f}\n")
    print(f"O valor do salário líquido é R$ {salarioLiquido:.2f}")
    print(f"O valor do FGTS depositado em conta é: R$ {fgts:.2f}")

elif salarioBruto > 1500 and salarioBruto <=2500:
    ir = salarioBruto * 0.10
    sindicato = salarioBruto*0.03
    inss = salarioBruto*0.10
    fgts = salarioBruto*0.11
    salarioLiquido = salarioBruto - sindicato - inss -ir
    print(f"Valor do Salário Bruto R$ {salarioBruto:.2f}")
    print(f"Valor do Sindicato     R$ {sindicato:.2f}")
    print(f"Valor do IR            R$ {ir:.2f}")
    print(f"Valor do INSS          R$ {inss:.2f}\n")
    print(f"O valor do salário líquido é R$ {salarioLiquido:.2f}")
    print(f"O valor do FGTS depositado em conta é: R$ {fgts:.2f}")

elif salarioBruto > 2500:
    ir = salarioBruto * 0.2
    sindicato = salarioBruto*0.03
    inss = salarioBruto*0.10
    fgts = salarioBruto*0.11
    salarioLiquido = salarioBruto - sindicato - inss -ir
    print(f"Valor do Salário Bruto R$ {salarioBruto:.2f}")
    print(f"Valor do Sindicato     R$ {sindicato:.2f}")
    print(f"Valor do IR            R$ {ir:.2f}")
    print(f"Valor do INSS          R$ {inss:.2f}\n")
    print(f"O valor do salário líquido é R$ {salarioLiquido:.2f}")
    print(f"O valor do FGTS depositado em conta é: R$ {fgts:.2f}")


#João recebeu seu salário de R$ 1200,00 e precisa pagar duas contas (C1=R$ 200,00 e C2=R$120,00) que estão atrasadas. 
# Como as contas estão atrasadas, João terá de pagar multa de 2% sobre cada conta. 
# Faça um algoritmo que calcule e mostre quanto restará do salário do João.


salario = float(input("Digite o valor do seu salário: \n"))
c1 = float(input("Valor da primeira conta: "))
c2 = float(input("Valor da segunda conta: \n"))
multa = 0.02
c1t = 200*0.02 #R$ 4,00
c2t = 120*0.02 #R$ 2,40
saldo = salario - (c1-c1t) - (c2-c2t)

print(f"O saldo do salario é: {saldo:.2f}")

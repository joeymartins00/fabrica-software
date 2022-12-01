#Faça um algoritmo que receba o preço de um produto, calcule e mostre o novo preço, sabendo-se que este sofreu um desconto de 10%.

bike = float(input("Digite o preço do produto: \n"))
desconto10 = float(input("Digite a porcentagem de desconto: \n"))

bike = 1500
desconto10 = 0.10
bike_com_desconto = bike-(bike*desconto10)

print(bike_com_desconto)
#A fábrica de refrigerantes Gui-Cola vende seu produto em três formatos: lata de 350 ml, garrafa de 600 ml e garrafa de 2 litros. 
# Se um comerciante compra uma determinada quantidade de cada formato, faça um algoritmo para calcular quantos litros de refrigerante ele comprou.​


lata = float(input("Digite a quantidade de latas que deseja comprar: "))
garrafa = float(input("Digite a quantidade de garrafas que deseja comprar: "))
pet = float(input("Digite a quantidade de pets que deseja comprar: "))

total = (lata*0.350)+(garrafa*0.600)+(pet*2)

print(lata,"litros")
print(garrafa,"litros")
print(pet,"litros")
print(total,"litros")
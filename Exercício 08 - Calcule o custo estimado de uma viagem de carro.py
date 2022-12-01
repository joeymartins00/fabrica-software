#Calcule o custo estimado de uma viagem de carro

valor_gasolina = float(input("Digite o preço da gasolina: \n"))
distancia_km = float(input("Digite a distancia em quilômetros que será percorrida: \n"))
autonomia = float(input("Digite a autonomia do veiculo: \n"))

quantidade_litros = distancia_km / autonomia
gastos_viagem = quantidade_litros*valor_gasolina

print("Valor gasto na viagem: \n", gastos_viagem)



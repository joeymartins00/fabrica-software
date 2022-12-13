#A lanchonete GostoSoft vende apenas um tipo de sanduíche, cujo recheio inclui duas fatias de queijo, uma fatia de presunto e uma rodela de hambúrguer.
# Sabendo que cada fatia de queijo ou presunto pesa 50 gramas, e que a rodela de hambúrguer pesa 100 gramas,
# faça um algoritmo em que o dono forneça a quantidade de sanduíches a fazer, e a máquina informe as quantidades (em quilos) de queijo, presunto e carne necessários para compra.

quantidade_sanduiche = float(input("Digite a quantidade de sanduiches a fazer: \n"))

queijo = 100
presunto = 50
hamburguer = 100

#sanduiche = queijo + presunto + hamburguer

queijo_kg = queijo/1000*quantidade_sanduiche
presunto_kg = presunto/1000*quantidade_sanduiche
hamburguer_kg = hamburguer/1000*quantidade_sanduiche
totalKg = queijo_kg + presunto_kg + hamburguer_kg

print("Quantidade total de queijo em Kg: ",queijo_kg)
print("Quantidade total de presunto em Kg: ",presunto_kg)
print("Quantidade total de hamburguer em Kg: ",hamburguer_kg)
print("Quantidade total em Kg: ",totalKg)
#O restaurante a quilo Sabor em Quilo cobra R$59,00 por cada quilo de refeição. 
# Escreva um algoritmo que leia o peso do prato montado pelo cliente (em quilos) e imprima o valor a pagar. 
# Assuma que a balança já desconte o peso do prato.​

peso_refeicao = float(input("Peso da refeição: \n"))
preco_kg = 59 
valor_pagar = peso_refeicao * 59

print(f"Peso da refeição {peso_refeicao}gr") 
print(f"Total a pagar R$ {valor_pagar:.2f}")


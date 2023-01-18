# Elabore um algoritmo que calcule o que deve ser pago por um produto, considerando o preço normal de etiqueta e a escolha da condição de pagamento. 
# Utilize os códigos da tabela a seguir para ler qual condição de pagamento escolhida e efetuar o cálculo adequado. ​

# Código Condição de pagamento: ​

#1 - À vista em dinheiro ou pix, recebe 10% de desconto;​
#2 - À vista no cartão de crédito, recebe 5% de desconto ​
#3 - Em duas vezes, preço normal de etiqueta sem juros ​
#4 - Em três vezes, preço normal de etiqueta mais juros de 10% ​

conta = float(input("Digite o valor a ser pago: \n"))
metodoPagamento = int(input("Escolha o método de pagamento: \n Digite \n 1 - À vista ou Pix \n 2 - Crédito À vista \n 3 - Duas Vezes \n 4 - Três Vezes \n"))

if metodoPagamento == 1:
    valortotal = conta-(0.10*conta)
    print(valortotal)

elif metodoPagamento == 2:
    valortotal = conta-(0.05*conta)
    print(valortotal)

elif metodoPagamento == 3:
    valortotal = conta
    print(valortotal)

elif metodoPagamento == 4:
    valortotal = conta+(0.10*conta)
    print(valortotal)


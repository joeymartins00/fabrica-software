#O cardápio da lanchonete Burgão é o seguinte: ​
#ESPECIFICAÇÃO CÓDIGO PREÇO ​
#Cachorro Quente       100            R$ 11,20 ​
#Ovo Simples               101           R$   8,30 ​
#Bauru com Ovo           102           R$ 11,50 ​
#Hambúrguer                103           R$ 16,20 ​
#Refrigerante                 201          R$ 6,00 ​
#Suco                            202           R$ 7,50 ​
#Água Mineral               203           R$ 4,70 ​
#Escreva um algoritmo que leia o código de um sanduíche e de uma bebida, e mostre o valor a pagar pelo cliente. Assuma as entradas correta: ​

#Cardápio da Lanchonete / Código / Preço.
print("Especificacao | Codigo | Preco") 
print("Cachorro Quente | 100 | R$ 11,20")
print("Ovo Simples | 101 | R$ 8,30")
print("Bauru com ovo | 102 | R$ 11,50")
print("Hamburguer | 103 | R$ 16,20")
print("Refrigerante | 201 | R$ 6,00")
print("Suco | 202 | R$ 7,50")
print("Àgua mineral | 203 | R$4,70")
#Variáveis
total = float(0) #Valor real
cont = 's' #Variável para continuar.
i = int(1) #Número do item no cupom.
while (cont == 's'): #Condição para continuar adicionando itens.
 item = int(input("Digite o codigo do pedido: ")) #Digitar código do pedido (número inteiro)
 qtd = int (input("Digite a quantidade: ")) #Digitar quantidade desejada (número inteiro)
 if (item == 100):#condição para item.
  preco = 11.20 #Preço de cada item.
 elif (item == 101): #Condições, caso contrária a condição anterior.
  preco = 8.30
 elif (item == 102):
  preco = 11.50
 elif (item == 103):
  preco = 16.20
 elif (item == 201):
  preco = 6.00
 elif (item == 202):
  preco = 7.50
 elif (item == 203):
  preco = 4.70
 else: #Se o código digitado não corresponder a nenhum código do cardápio.
  print("Codigo invalido")
  total = 0.00
  break #Finaliza o programa e os pedidos anteriores com valor R$ 0.00. 
 val = float(qtd * preco) #Preço de cada item.
 print("%d  %d  %d  %.2f = %.2f" % (i, item, qtd, preco, val))#Impressão dos itens/quantidades/valores no cupom.
 total += val #Valor Total da compra (Soma de todos os valores).
 i += 1 #Número do item em ordem crescente.
 cont = input("Deseja fazer mais pedidos? [s/n]:")#Selecionar adicionar item ou não.
print("Total da compra: %.2f" % (total))#Mostra o valor total da compra.
print ("Agradecemos a preferencia!")
print ("--------------------FIM------------------")
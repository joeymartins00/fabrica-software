 #A padaria Super Pão vende uma certa quantidade de pães franceses e uma quantidade de broas a cada dia. 
 # Cada pãozinho custa R$ 1,00 e a broa custa R$ 3,50. 
 # Ao final do dia, o dono quer saber quanto arrecadou com a venda dos pães e broas (juntos), e quanto deve guardar numa conta de poupança (10% do total arrecadado). 
 # Você foi contratado para fazer os cálculos para o dono. 
 # Com base nestes fatos, faça um algoritmo para ler as quantidades de pães e de broas, e depois calcular os dados solicitados. ​

quantidadeP = float(input("Digite a quantidade de pães vendidos: \n"))
quantidadeB = float(input("Digite a quantidade de broas vendidas: \n"))

paes = 1.0
broas = 3.5

#porcentagem guardada na poupança é 10%

porcentagem = 0.10
total_vendido = (quantidadeP+quantidadeB)*(paes+broas)
total_poupanca = total_vendido*porcentagem

print(f"Quantidade de pães vendidos {quantidadeP:.1f}")
print(f"Quantidade de broas vendidas {quantidadeB:.1f}")
print(f"Valor total vendido {total_vendido:.2f}")
print(f"Valor total poupado {total_poupanca:.2f}")
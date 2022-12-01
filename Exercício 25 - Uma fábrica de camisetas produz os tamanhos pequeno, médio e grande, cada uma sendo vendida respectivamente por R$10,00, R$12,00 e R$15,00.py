#Uma fábrica de camisetas produz os tamanhos pequeno, médio e grande, cada uma sendo vendida respectivamente por R$10,00, R$12,00 e R$15,00.
# Faça um algoritmo em que o usuário forneça a quantidade de camisetas pequenas, médias e grandes referentes a uma venda, o algoritmo informe qual o valor total da compra.

QC = float(input("Digite a quantidade de camisetas: \n"))

P = 10 * QC
M = 12 * QC
G = 15 * QC

print("Quantidade de camisetas P: ", P)
print("Quantidade de camisetas M: ", M)
print("Quantidade de camisetas G: ", G)

valor_total = (P + M + G)

print("Valor Total da Compra:", valor_total)
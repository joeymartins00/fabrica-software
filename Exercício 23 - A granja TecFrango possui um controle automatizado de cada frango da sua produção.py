#A granja TecFrango possui um controle automatizado de cada frango da sua produção.
# No pé direito do frango há um anel com um chip de identificação, no pé esquerdo são dois anéis para indicar o tipo de alimento que ele deve consumir.
# Sabendo que o anel com chip custa R$ 4,00 e o anel de alimento custa R$ 3,50,
# faça um algoritmo para calcular o gasto total da granja (com base na quantidade de frangos digitada pelo usuário) para marcar todos os seus frangos.

total_frangos = float(input("Digite a quantidade de frangos a ser calculada: \n"))
anel_identificacao = float(input("Digite o preço do anel de identificação: \n"))
anel_alimento = float(input("Digite o preço do anel de alimentação: \n"))


anel_identificacao = 4
anel_alimento = 7
preco_por_animal = anel_identificacao+anel_alimento

preco_final = preco_por_animal*total_frangos

print(preco_por_animal)
print(preco_final)
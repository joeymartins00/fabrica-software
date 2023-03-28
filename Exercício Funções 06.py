'''6 – Um comerciante possui uma loja de artigos de R$ 1,99. 
Para agilizar o cálculo de quanto cada cliente deve pagar 
ele desenvolveu uma tabela que contém o número de itens que o cliente comprou e ao lado o valor
da conta. 
Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e 
olhar na tabela de preços. 
Você foi contratado para desenvolver uma função que monta esta tabela de preços, que conterá os 
preços de 1 até 50 produtos, conforme o exemplo abaixo:

Loja Quase Dois - Tabela de preços
1- R$ 1.99
2- R$ 3.98
...
50-- R$ 99.50'''


def precos(num):
    lista = []
    for i in range(1,51):
        lista.append(i*1.99)
    return lista[num-1]


consulta = precos(50)

print(consulta)
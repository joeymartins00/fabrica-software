#Entrar com o dia e o mês de uma data e informar quantos dias se passaram desde o início do ano. 
#Esqueça a questão dos anos bissextos e considere sempre que um mês possui 30 dias. ​

dia = int(input("Digite o dia: \n"))
mes = int(input("Digite o mes: \n"))

dias_passados = ((mes-1) * 30) + dia-1

# 01 de janeiro - 0 dias desde o início do ano
# 01 de fevereiro - 30 dias desde o início do ano
# 02 de março - 61 dias desde o início do ano


print(f"Já se passaram {dias_passados} dias desde o início do ano.")
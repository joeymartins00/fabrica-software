#Faça um algoritmo que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre: 
# a) a idade dessa pessoa em anos; 
# b) a idade dessa pessoa em meses; 
# c) a idade dessa pessoa em dias; 
# d) a idade dessa pessoa em semanas

hora = 60
dia = 24 * hora
semana = 7 * dia
mes = 30 * dia
ano = 12 * mes

ano_nascimento = int(input("Digite o ano de nascimento: ")) 
ano_atual = int(input("Digite o ano atual: "))
idade = ano_atual - ano_nascimento
idade_anos = idade*365
idade_meses = idade_anos*12
idade_semanas = idade_meses/7
idade_dias = idade_meses*30

print('Idade em anos é ', idade_anos)
print('Idade em meses é ', idade_meses)
print('Idade em dias é ', idade_dias)
print('Idade em semanas é ', idade_semanas)


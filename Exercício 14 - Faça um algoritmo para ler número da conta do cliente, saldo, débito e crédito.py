#Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito.
#Após, calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito).
#Também testar se saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo', senão escrever a mensagem 'Saldo Negativo' .

num_conta_cliente = input("Digite o número da conta do cliente: \n")
saldo = float(input("Digite o saldo da conta do cliente: \n"))
debito = float(input("Digite o débito da conta do cliente: \n"))
credito = float(input("Digite o credito do conta do cliente; \n"))

saldo_atual = (saldo-debito+credito)

if saldo_atual >= 0:
    print("Saldo Positivo")

else:
    print("Saldo Negativo")
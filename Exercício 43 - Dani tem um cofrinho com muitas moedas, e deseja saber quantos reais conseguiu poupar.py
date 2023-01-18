#Dani tem um cofrinho com muitas moedas, e deseja saber quantos reais conseguiu poupar. 
#Faça um algoritmo para ler a quantidade de cada tipo de moeda, e imprimir o valor total economizado, em reais.  
# Considere que existam moedas de 1, 5, 10, 25 e 50 centavos, e ainda moedas de 1 real. 
# Não havendo moeda de um tipo, a quantidade respectiva é zero. ​

centavo1 = float(input("Digite a quantidade de moedas de um centavo: "))
centavos5 = float(input("Digite a quantidade de moedas de 5 centavos: "))
centavos10 = float(input("Digite a quantidade de moedas de 10 centavos: "))
centavos25 = float(input("Digite a quantidade de moedas de 25 centavos: "))
centavos50 = float(input("Digite a quantidade de moedas de 50 centavos: "))
real1 = float(input("Digite a quantidade de moedas de 1 real: "))
totalPoupado = (centavo1*0.01)+(centavos5*0.05)+(centavos10*0.10)+(centavos25*0.25)+(centavos50*0.50)+(real1*1)
print(totalPoupado)



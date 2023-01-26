#Ler diversos números e exibir qual foi a soma. O valor -999 é o código de fim da  entrada. ​
soma = 0
num = 0 
while num != -999:
    soma += num
    num = int(input("Digite um número: "))

print(soma)

    
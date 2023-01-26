#Ler 20 números e exibir qual foi o menor e o maior informados. ​
num = int(input("Digite um número: "))
menor = num
maior = num
for i in range(1,20):
    num = int(input("Digite um número: "))
    if num < menor:
        menor = num
    elif num > maior:
        maior = num
print(f'O menor número digitado foi: {menor}.')
print(f'O maior número digitado foi: {maior}.') 
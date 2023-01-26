#Ler diversos números inteiros e exibir quantas vezes o número 50 foi informado. O valor 0 é o código de fim de entrada.
num = int(input("Digite um número: "))
contador = 0
while num != 0:
    if num == 50:
        contador += 1
    num = int(input("Digite um número: "))
print(f"A quantidade de vezes que o número 50 apareceu foi: {contador}")

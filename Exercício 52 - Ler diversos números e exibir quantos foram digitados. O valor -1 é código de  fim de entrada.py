#Ler diversos números e exibir quantos foram digitados. O valor -1 é código de  fim de entrada.
contador = 0
num = int(input("Digite um número: "))
while num != -1:
    contador += 1
    num = int(input("Digite um número: "))
print(contador)
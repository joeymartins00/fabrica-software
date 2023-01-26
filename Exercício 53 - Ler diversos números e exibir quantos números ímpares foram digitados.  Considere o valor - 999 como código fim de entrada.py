#Ler diversos números e exibir quantos números ímpares foram digitados.  Considere o valor - 999 como código fim de entrada.​
#Ler diversos números e exibir quantos números ímpares foram digitados.  Considere o valor - 999 como código fim de entrada.
num = int(input("Digite um número: "))
impar = 0
while num != -999:
    if num %2 == 1:
        impar += 1
    num = int(input("Digite um número: "))
print(f"A quantidade de números ímpares foram: {impar}")
    
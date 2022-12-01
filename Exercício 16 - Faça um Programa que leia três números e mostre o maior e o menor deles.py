#Faça um Programa que leia três números e mostre o maior e o menor deles.

n1 = int(input("Digite o primeiro número: \n"))
n2 = int(input("Digite o segundo número: \n"))
n3 = int(input("Digite o terceiro número: \n"))

if n1<n2 and n1<n3 :
    print(f"{n1} é menor do que {n2} e {n3}")

if n2<n1 and n2<n3 :
    print(f"{n2} é menor do que {n1} e {n3}")

if n3<n1 and n3<n2 :
    print(f"{n3} é menor do que {n1} e {n2}")

if n1>n2 and n1>n3 :
    print(f"{n1} é maior do que {n2} e {n3}")

if n2>n1 and n2>n3 :
    print(f"{n2} é maior do que {n1} e {n3}")

if n3>n1 and n3>n2 :
    print(f"{n3} é maior do que {n1} e {n2}")


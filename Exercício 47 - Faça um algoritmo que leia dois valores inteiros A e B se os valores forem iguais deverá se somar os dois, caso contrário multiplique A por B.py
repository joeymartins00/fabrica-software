#Faça um algoritmo que leia dois valores inteiros A e B se os valores forem iguais deverá se somar os dois, caso contrário multiplique A por B. 
# Ao final de qualquer um dos cálculos deve-se atribuir o resultado para uma variável C e mostrar seu conteúdo na tela.​
valA = int(input('Digite um número: '))
valB = int(input('Digite um número: '))
soma = valA+valB
multiplicar = valA*valB

if valA == valB:
    print(soma)

else:
    print(multiplicar)
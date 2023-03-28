'''4 – Escreva um programa, com uma função que necessite de um argumento. 
A função retornar o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.'''
x = int(input("Digite um valor para x: "))
def questao(x):
    while True:
        if x > 0:
            print("positivo")
        else:
            print("Negativo")
        return x
        break
valorX = questao(x)
print("Pois o valor de X é",valorX)
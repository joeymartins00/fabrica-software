'''4 – Escreva um programa, com uma função que necessite de um argumento. 
A função retornar o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.'''

def headbanger(num):
    if num > 0:
        return "Positivo"
    else:
        return "Negativo"
bulltigus = headbanger(int(input("Digite um número: ")))
print(bulltigus)
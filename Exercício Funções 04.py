'''4 – Escreva um programa, com uma função que necessite de um argumento. 
A função retornar o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.'''

#headbanger é o nome da função; num é o argumento; bulltigus é o nome da variável;

def headbanger(num):
    if num > 0:
        return "P"
    else:
        return "N"
bulltigus = headbanger(int(input("Digite um número: ")))
print(bulltigus)
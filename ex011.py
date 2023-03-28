'''11 - Crie uma função que receba como argumento uma lista, com valores de qualquer tipo. 
A função deve imprimir todos os elementos da lista numerando-os. 
Exemplo:
1, Pera
2, Uva
3, Maça
4, Salada mista '''

frutas=["Banana","Melancia","Mamão"]
frutas.append("Pêra")
frutas.append("Uva")
frutas.append("Maçã")
frutas.append("Salada Mista")

def imprimirFrutas(lista):
    contador=0
    for item in lista:
        contador+=1

        print(contador, item)

imprimirFrutas(frutas)


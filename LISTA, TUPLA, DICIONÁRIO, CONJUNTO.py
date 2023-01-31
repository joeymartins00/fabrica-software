'''DEFINIÇÃO DE LISTA - TUPLA - DICIONARIO - CONJUNTO'''

#LISTA É UMA COLEÇÃO ORDENADA E MUTÁVEL. PERMITE MEMBROS DUPLICADOS.
lista = ["carro", True, 2, 3.5]
print(lista)
print(type(lista))
print('*'*30)

#TUPLA É UMA COLEÇÃO ORDENADA E IMUTÁVEL. PERMITE MEMBROS DUPLICADOS.
tupla("carro", True, 2, 3.5)
print(tupla)
print(type(tupla))
print('*'*30)
             
#O DICIONÁRIO É UMA COLEÇÃO ORDENADA E MUTÁVEL. NENHUM MEMBRO PODE SER DUPLICADO.
             #chave:  #valor
dicionario = {"nome": "carro", "logica": True, "numero": 2, "outroNumero": 3.5}
print(dicionario)
print(type(dicionario))
print('*'*30)

#SET (OU CONJUNTO) É UMA COLEÇÃO NÃO ORDENADA E NÃO INDEXADA. NENHUM MEMBRO PODE SER DUPLICADO.
conjunto = {"carro", True, 2, 3.5}
print(conjunto)
print(type(conjunto))

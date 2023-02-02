'''Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:​
Código da cidade;​
Número de veículos de passeio (em 1999);​
Número de acidentes de trânsito com vítimas (em 1999). ​
Deseja-se saber:​
Qual o maior e menor índice de acidentes de transito e a que cidade pertence;​
Qual a média de veículos nas cinco cidades juntas;​
Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.​'''
cod = int(input('Digite o código da cidade: '))
veiculos = float(input('Digite a quantidade de veiculos de passeio: '))
acidentes = float(input('Digite o número de acidentes de trânsito com vítimas: '))
codCidadeMenor = codCidadeMaior = cod
maior = menor = acidentes
soma = veiculos
somaAcidentes = cont = 0
for c in range(0,2):
    soma += veiculos
    cod = int(input('Digite o código da cidade: '))
    veiculos = float(input('Digite a quantidade de veiculos de passeio: '))
    acidentes = float(input('Digite o número de acidentes de trâmsito com vítimas: '))

    if acidentes > maior:
        maior = acidentes
        codCidadeMaior = cod

    if acidentes < menor:
        menor = acidentes
        codCidadeMenor = cod

    if veiculos <= 2000:
        somaAcidentes += acidentes
        cont += 1
print(f'O código da cidade com menor indice de acidentes é {codCidadeMenor} com {menor} acidentes')
print(f'O código da cidade com maior indice de acidentes é {codCidadeMaior} com {maior} acidentes')
print(f'A média dos veiculos das cinco cidades é: {soma/5}')
    
    #SEGUNDA FORMA DE FAZER MAIS DESCRITIVA:
    
maiorAcidente = 0
menorAcidente = 10000000
mediaAcidentes = 0
contador = 0
contador1 = 0
somaAcidentes = 0
mediaMenor2000 = 0
somaMenor2000 = 0
for i in range(5):
    cod = int(input("Digite o código da cidade: "))
    numVeiculosPasseio = int(input("Digite o número de veiculos de passeio em 1999: "))
    numAcidentesTransito = int(input("Digite o número de acidentes de trânsito em 1999: "))
    if numAcidentesTransito > maiorAcidente:
        maiorAcidente = numAcidentesTransito
        codMaior = cod
    if numAcidentesTransito < menorAcidente:
        menorAcidente = numAcidentesTransito
        codMenor = cod
    somaAcidentes = somaAcidentes+numAcidentesTransito
    contador += 1
    if numVeiculosPasseio < 2000:
        somaMenor2000 = somaMenor2000+numAcidentesTransito
        contador1 += 1
mediaMenor2000 = somaMenor2000/contador1
mediaAcidentes = somaAcidentes/5 
mediaVeiculos = numVeiculosPasseio/5
print(f"O menor índice de acidentes foi de {menorAcidente:.1f} e a cidade com o menor índice foi {codMenor:.1f}")
print(f"O maior índice de acidentes foi de {maiorAcidente:.1f} e a cidade com o maior índice foi {codMaior:.1f}")
print(f"A média de veículos nas cinco cidades juntas foi de {mediaVeiculos:.1f}")
print(f"A média de acidentes nas cidades co menos de 2000 veículos de passeio foi de {mediaAcidentes:.1f}")

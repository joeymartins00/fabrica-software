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
    
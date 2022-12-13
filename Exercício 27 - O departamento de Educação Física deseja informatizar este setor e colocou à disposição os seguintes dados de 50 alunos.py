#O departamento de Educação Física deseja informatizar este setor e colocou à disposição os seguintes dados de 50 alunos:
#Matrícula, sexo (M, F), altura (cm) e status físico (1–bom, 2–regular, 3–ruim)
#Estes dados deverão ser lidos através de uma unidade de entrada qualquer.
#Calcular e imprimir:
#a) A quantidade de alunos do sexo feminino com altura superior a 170 cm.
#b) A % de alunos do sexo masculino (em relação ao total de alunos do sexo masculino) cujo status físico seja bom.

alunos = 0
totalmulheres = 0
totalhomens = 0
bons = 0
porcentagem = 0

while alunos < 5:
    sexo = input("Digite o sexo: ")
    altura = input("Digite a altura: ")
    status = input("1 - BOM / 2 - REGULAR / 3 RUIM: ")

    if(sexo == "F" and altura > 1.7):
        totalmulheres = totalmulheres + 1
        
    else:
        totalhomens = totalhomens + 1

    if(sexo == "M" and status == 1):
        bons = bons + 1
        porcentagem = bons * 100 / totalhomens

    alunos = alunos + 1

print("Total de Mulheres altas: ",totalmulheres)
print("Porcentagem de homens bons: ",porcentagem)
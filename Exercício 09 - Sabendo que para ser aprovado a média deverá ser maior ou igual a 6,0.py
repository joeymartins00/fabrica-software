#Faça um algoritmo que leia o nome do aluno, o nome da disciplina, notas de 3 provas e calcule a média de um aluno e verifique se o aluno foi aprovando.
# Sabendo que para ser aprovado a média deverá ser maior ou igual a 6,0.

nome_aluno = input("Digite o nome do aluno: \n")
nome_disciplina = input("Digite o nome da disciplina: \n")
nota1 = float(input("Digite a nota da prova 1: \n"))
nota2 = float(input("Digite a nota da prova 2: \n"))
nota3 = float(input("Digite a nota da prova 3: \n"))

media = (nota1+nota2+nota3)/3

if media >= 6:
    print(f"O Aluno está aprovado com média {media}")
else:
    print(f"O Aluno está reprovado com média {media}")
    



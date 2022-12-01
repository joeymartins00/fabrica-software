nome_aluno = input("Digite o nome do aluno: \n")
print("1 - Português")
print("2 - Matemática")
print("3 - Geografia")
print("4 - História")
materia = int(input("Digite o número referente a matéria: \n"))

pb1_portugues = 0.0
pb2_portugues = 0.0
pb3_portugues = 0.0
pb4_portugues = 0.0
pb1_matematica = 0.0
pb2_matematica = 0.0
pb3_matematica = 0.0
pb4_matematica =0.0
pb1_geografia = 0.0
pb2_geografia = 0.0
pb3_geografia = 0.0
pb4_geografia = 0.0
pb1_historia = 0.0
pb2_historia = 0.0
pb3_historia = 0.0
pb4_historia = 0.0

if materia == 1:
    pb1_portugues = float(input("Digite a nota da prova de Portugues Primeiro Bimestre: \n"))
    pb2_portugues = float(input("Digite a nota da prova de Portugues Segundo Bimestre: \n"))
    pb3_portugues = float(input("Digite a nota da prova de Portugues Terceiro Bimestre: \n"))
    pb4_portugues = float(input("Digite a nota da prova de Portugues Quarto Bimestre: \n"))

elif materia == 2:
    pb1_matematica = float(input("Digite a nota da prova de Matemática Primeiro Bimestre: \n"))
    pb2_matematica = float(input("Digite a nota da prova de Matemática Segundo Bimestre: \n"))
    pb3_matematica = float(input("Digite a nota da prova de Matemática Terceiro Bimestre: \n"))
    pb4_matematica = float(input("Digite a nota da prova de Matemática Quarto Bimestre: \n"))

elif materia == 3:
    pb1_geografia = float(input("Digite a nota da prova de Geografia Primeiro Bimestre: \n"))
    pb2_geografia = float(input("Digite a nota da prova de Geografia Segundo Bimestre: \n"))
    pb3_geografia = float(input("Digite a nota da prova de Geografia Terceiro Bimestre: \n"))
    pb4_geografia = float(input("Digite a nota da prova de Geografia Quarto Bimestre: \n"))

elif materia == 4:
    pb1_historia = float(input("Digite a nota da prova de História Primeiro Bimestre: \n"))
    pb2_historia = float(input("Digite a nota da prova de História Segundo Bimestre: \n"))
    pb3_historia = float(input("Digite a nota da prova de História Terceiro Bimestre: \n"))
    pb4_historia = float(input("Digite a nota da prova de História Quarto Bimestre: \n"))

media_portugues = (pb1_portugues + pb2_portugues + pb3_portugues + pb4_portugues) / 4
media_matematica = (pb1_matematica + pb2_matematica + pb3_matematica + pb4_matematica) / 4
media_geografia = (pb1_geografia + pb2_geografia + pb3_geografia + pb4_geografia) / 4
media_historia = (pb1_historia + pb2_historia + pb3_historia + pb4_historia) / 4

media_final_total = (media_portugues + media_matematica + media_geografia + media_historia) / 4

print("Nome do aluno: \n", nome_aluno)

print("Português: \n")
print("Nota da Prova de Portugues Primeiro Bimestre: \n", pb1_portugues)
print("Nota da Prova de Portugues Segundo Bimestre: \n", pb2_portugues)
print("Nota da Prova de Portugues Terceiro Bimestre: \n", pb3_portugues)
print("Nota da Prova de Portugues Quarto Bimestre: \n", pb4_portugues)

print("Matemática: \n")
print("Nota da Prova de Matemática Primeiro Bimestre: \n", pb1_matematica)
print("Nota da Prova de Matemática Segundo Bimestre: \n", pb2_matematica)
print("Nota da Prova de Matemática Terceiro Bimestre: \n", pb3_matematica)
print("Nota da Prova de Matemática Quarto Bimestre: \n", pb4_matematica)

print("Geografia: \n")
print("Nota da Prova de Geografia Primeiro Bimestre: \n", pb1_geografia)
print("Nota da Prova de Geografia Segundo Bimestre: \n", pb2_geografia)
print("Nota da Prova de Geografia Terceiro Bimestre: \n", pb3_geografia)
print("Nota da Prova de Geografia Quarto Bimestre: \n", pb4_geografia)

print("História: \n")
print("Nota da Prova de História Primeiro Bimestre: \n", pb1_historia)
print("Nota da Prova de História Segundo Bimestre: \n", pb2_historia)
print("Nota da Prova de História Terceiro Bimestre: \n", pb3_historia)
print("Nota da Prova de História Quarto Bimestre: \n", pb4_historia)

print("Média Final de Português: \n", media_portugues)
print("Média Final de Matemática: \n", media_matematica)
print("Média Final de Geografia: \n", media_geografia)
print("Média Final de História: \n", media_historia)

if media_portugues >= 6:
    print(
        f"As notas foram: {pb1_portugues},{pb2_portugues},{pb3_portugues} e {pb4_portugues} a Média de Português do aluno "f" {nome_aluno} foi {media_portugues:.2f}), foi suficiente para ser aprovado.\n")

else:
    print(
        f"As notas foram: {pb1_portugues},{pb2_portugues},{pb3_portugues} e {pb4_portugues} a Média de Português do aluno "f" {nome_aluno} foi {media_portugues:.2f}), NÃO foi suficiente para ser aprovado.\n")

if media_matematica >= 6:
    print(
        f"As notas foram: {pb1_matematica},{pb2_matematica},{pb3_matematica} e {pb4_matematica} a Média de Matemática do aluno "f" {nome_aluno} foi {media_matematica:.2f}), foi suficiente para ser aprovado.\n")

else:
    print(
        f"As notas foram: {pb1_matematica},{pb2_matematica},{pb3_matematica} e {pb4_matematica} a Média de Matemática do aluno "f" {nome_aluno} foi {media_matematica:.2f}), NÃO foi suficiente para ser aprovado.\n")

if media_geografia >= 6:
    print(
        f"As notas foram: {pb1_geografia},{pb2_geografia},{pb3_geografia} e {pb4_geografia} a Média de Geografia do aluno "f" {nome_aluno} foi {media_geografia:.2f}), foi suficiente para ser aprovado.\n")

else:
    print(
        f"As notas foram: {pb1_geografia},{pb2_geografia},{pb3_geografia} e {pb4_geografia} a Média de Geografia do aluno "f" {nome_aluno} foi {media_geografia:.2f}), NÃO foi suficiente para ser aprovado.\n")

if media_historia >= 6:
    print(
        f"As notas foram: {pb1_historia},{pb2_historia},{pb3_historia} e {pb4_historia} a Média de História do aluno "f" {nome_aluno} foi {media_historia:.2f}), foi suficiente para ser aprovado.\n")

else:
    print(
        f"As notas foram: {pb1_historia},{pb2_historia},{pb3_historia} e {pb4_historia} a Média de História do aluno "f" {nome_aluno} foi {media_historia:.2f}), NÃO foi suficiente para ser aprovado.\n")

if media_final_total >= 6:
    print(
        f"A média final total do aluno {nome_aluno} foi {media_final_total:.2f}, foi suficiente para ser aprovado no Colégio Militar: \n")

else:
    print(
        f"A média final total do aluno {nome_aluno} foi {media_final_total:.2f}, NÃO foi suficiente para ser aprovado no Colégio Militar: \n")
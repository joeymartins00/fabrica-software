#nome do aluno, nome da disciplina,nota de 3 provas e calcule a média

nome = input("Digite o nome do aluno: \n")
disciplina = (input("Digite o nome da matéria: \n"))
prova1 = float(input("Digite prova B1: \n"))
prova2 = float(input("Digite prova B2: \n"))
prova3 = float(input("Digite prova B3: \n"))

media = (prova1+prova2+prova3)/3

print("Nome do Aluno: \n",nome)
print("Matéria: \n",disciplina)
print("Prova B1: \n",prova1)
print("Prova B2: \n",prova2)
print("Prova B3: \n",prova3)

print("Média: \n",media)

print(f"A média do aluno {nome} foi {media:.2f}, foi suficiente para ser aprovado: \n")

if(media>= 6):
    print(f"As notas foram: {prova1},{prova2} e {prova3} Média do aluno "f" aluno {nome} foi {media:.2f}, foi o suficiente para passar.")


else:
    print(f"As notas foram: {prova1}, {prova2} e {prova3} Média "f" do aluno {nome} foi {media:.2f}, Não foi o suficiente para passar.")





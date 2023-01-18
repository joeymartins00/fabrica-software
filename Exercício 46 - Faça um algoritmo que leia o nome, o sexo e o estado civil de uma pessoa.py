#Faça um algoritmo que leia o nome, o sexo e o estado civil de uma pessoa. 
#Caso sexo seja “F” e estado civil seja “CASADA”, solicitar o tempo de casada (anos).

nome = input("DIGITE SEU NOME: ")
sexo= input("DIGITE SEU SEXO\n 1- [F]\n 2- [M]: ")
estado_civil = input("DIGITE SEU ESTADO CIVIL\n 1- [SOLTEIRA]\n 2- [SOLTEIRO]\n 3- [CASADA]\n 4- [CASADO]\n 5- [DIVORCIADA]\n 6- [DIVORCIADO]\n 7- [UNIÃO ESTÁVEL]: ")
tempo_de_relacionamento = 0

if sexo == "1" and estado_civil =="3":
    tempo_de_relacionamento = input("DIGITE O TEMPO DE RELACIONAMENTO: ")
    print(f"{tempo_de_relacionamento} ANOS")

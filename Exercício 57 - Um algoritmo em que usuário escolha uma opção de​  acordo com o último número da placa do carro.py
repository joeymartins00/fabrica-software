'''Um algoritmo em que usuário escolha uma opção de acordo com o último número da placa do carro e mostre uma mensagem dizendo em que dia​ da semana não poderá circular.​

0 - 1 “Não Circular 2ª Feira”​

2 - 3 “Não Circular 3ª Feira”​

4 - 5 “Não Circular 4ª Feira”​

6 - 7 “Não Circular 5ª Feira”​

8 - 9 “Não Circular 6ª Feira”​. '''
placa = input("Digite sua placa: ")
print(placa[-1])
i = placa[-1]
if i == '0' or i == '1':
    print("Não circular 2ª feira")
if i == '2' or i == '3':
    print("Não circular 3ª feira")
if i == '4' or i == '5':
    print("Não circular 4ª feira")
if i == '6' or i == '7':
    print("Não circular 5ª feira")
if i == '8' or i == '9':
    print("Não circular 6ª feira")

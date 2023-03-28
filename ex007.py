'''7 - Crie uma função que efetue o cálculo do salário e como retorno teremos o valor a ser pago conforme o número de horas trabalhadas.
Considere a carga horária de 40h por semana como salário base, caso ultrapasse o limite de 40h, 
o funcionário deve receber 50% a mais por hora excedente.'''


salarioBase = float(input("Digite o seu salário: "))
qtdHorasTrabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))
salarioTotal = salarioTotal(salarioBase*qtdHorasTrabalhadas)
if qtdHorasTrabalhadas > 30:
    print(salario)
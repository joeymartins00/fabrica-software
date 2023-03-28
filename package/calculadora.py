class Calculadora:

    pass

    def calcular(self,opcao,num1,num2):
        if opcao == "*":
            return self.__multiplicar(num1,num2)
        elif opcao == "/":
            return self.__dividir(num1,num2)
        else:
            print("Opção inválida!")

    
    def __multiplicar(self,n1,n2):
        return n1*n2
    
    def __dividir(self,n1,n2):
        return n1/n2
    
calculo = Calculadora()
resultado = calculo.calcular("*",20,30)
print(resultado)

calculo = Calculadora()
resultado = calculo.calcular("/",60,30)
print(resultado)
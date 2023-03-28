'''2 – Crie uma função para calcular a exponenciação, que necessite dois argumentos e apresente como resultado a potência. 
Sendo base elevado ao expoente.'''
def exponenciacao(k,p):
    calculo = k**p
    return calculo
    
resultado = exponenciacao(2,3)
print(f'O resultado da exponenciação é {resultado}')
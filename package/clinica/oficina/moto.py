class Veiculo:
    def __init__(self,marca,modelo,ano):
        self.marca = marca 
        self.modelo = modelo
        self.ano = ano

    def transitar(self):
        return (f"{self.modelo} andou.")
    
v1 = Veiculo("Toyota","Hilux",2023)
print(v1.transitar())


class Jato(Veiculo):
    def __init__(self,marca,modelo,ano,potencia):
        super().__init__(marca,modelo,ano)
        self.potencia = potencia

    def transitar(self):
        return (f"{self.modelo} voou.")
    
jatinho = Jato("Vortex","Hellfire","1957","40.000")
print(jatinho.transitar())
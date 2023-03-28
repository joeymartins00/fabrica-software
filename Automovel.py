class Automovel:
    def __init__(self,placa="HSB-9999"):
        self.placa = placa

    def dirigir(self,velocidade):
        print(f"Estou dirigindo a {velocidade} km/h")

    def get_placa(self):
        print(f"A placa multada é {self.placa}")

car1 = Automovel()
car1.get_placa()
car1.dirigir(60)

car2 = Automovel("HSZ-8176")
car2.get_placa()
car2.dirigir(95)



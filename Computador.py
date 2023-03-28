class Computador:
    def __init__(self,marca,modelo,processador,memoria,ssd,placavideo,preco):
        self.marca = marca
        self.modelo = modelo
        self.processador = processador
        self.memoria = memoria
        self.ssd = ssd
        self.placavideo = placavideo
        self.preco = preco

#Get(Buscando valor)

    def get_marca(self):
        return self.marca
    
    def get_preco(self):
        return self.preco
    
#Set(Alterando valor)

    def set_preco(self, novo_preco):
        self.preco = novo_preco

notebook = Computador("ASUS","Note2023","Core i5","12GB","1TB","RTX 4080",3600)
preco = notebook.get_preco()
print("Preço atual é R$",notebook.get_preco())

notebook.set_preco(2900)
preco2 = notebook.get_preco()
print("O preco na promoção é RS",preco2)
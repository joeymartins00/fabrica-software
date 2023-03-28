class Contador:
    def __init__(self):
        self.cont = 0

    def reset(self):
        if self.cont > 0:
            self.cont = 0

    def increment(self):
        self.cont += 1

    def get_status(self):
        return self.cont
    
if __name__ == "__main__":
    contador = Contador()
    for i in range(1,11):
        contador.increment()
    print(contador.get_status())
    contador.reset()
    print(contador.get_status())
   


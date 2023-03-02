def sair(tempo):
    if tempo == "CHUVA":
        return "Levar guarda chuva"
    else:
        return "BORA!!"
    
role = sair("SOL")
print(role)
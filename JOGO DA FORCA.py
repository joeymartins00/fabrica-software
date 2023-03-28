import random 

def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
#JOGO DA FORCA COMPLETO

palavra_secreta = ["F","A","B","R","I","C","A"," ","D","E"," ","S","O","F","T","W","A","R","E"]
letras_descobertas = []

print("\n*** JOGO DA FORCA ***\n")

for i in range(0, len(palavra_secreta)) :
    letras_descobertas.append("-")
    
acertou = False

while acertou == False :
    letra = str(input("Digite a letra: ")).upper()
    
    for i in range(0, len(palavra_secreta)) :
            if letra == palavra_secreta[i] :
                letras_descobertas[i] = letra
                
            print(letras_descobertas[i])
            
    acertou = True 
        
    for x in range(0, len(letras_descobertas)) :
        if letras_descobertas[x] == "-" :
            acertou = False
            
            
print("PARABÉNS VOCÊ ENCONTROU A PALAVRA SECRETA!")
imprime_mensagem_vencedor()




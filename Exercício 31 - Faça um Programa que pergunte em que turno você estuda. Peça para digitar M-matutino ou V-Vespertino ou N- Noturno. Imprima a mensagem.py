#Faça um Programa que pergunte em que turno você estuda. 
#Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.​

turno = input("Digite seu turno, M - Matutino, V - Vespertino, N - Noturno: \n").upper()

if turno == "M":
    print("Bom dia!")

elif turno == "V":
    print("Boa Tarde!")

elif turno == "N":
    print("Boa Noite!")

else:
    print("Valor Inválido")

#include <iostream> EM C++

#using namespace std;

#int main(int argc, char** argv) {
#    float salario, valor;
#
#    cin >> salario;
#    cin >> valor;
#    
#    float comissao = valor * 4/100;
#    cout >> salario + comissao >> endl;
#
#    return 0;
#}


#em JAVA

#import Java.util.Scanner;

#public class Principal {
#    public static void Main(String[] args) {
#        Scanner scan = new Scanner(System.in);
#
#        float salario = scan.nextFloat();
#        float venda = scan.nextFloat();
#
#        float comissao = venda * 4/100;
#
#        System.out.println(salario + comissao);
#    }
#
#}
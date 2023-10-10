#Desenvolva um programa que só deve aceitar números pares. Siga as seguintes instruções:

#caso um número ímpar seja digitado, informe ao usuário que ele digitou um valor ímpar e peça novamente por um número par;

#caso uma letra seja digitada, informe ao usuário que ele digitou um caractere inválido e peça novamente por um número par.

def numerosPares(num1):
    if num1 %2 ==0:
        print('O número informado é par')
    else:
        print('O número informado é impar')
   
    
 

numerosPares(7)

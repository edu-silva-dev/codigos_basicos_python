#Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
#A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).

#Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.

def nomeIdade():
    nome = str(input('Informe seu nome '))
    ano = int(input('Informe o ano de nascimento '))
    if (ano >= 1992) and (ano <=2021):
        calc = 2021 - ano
        print(f'Seu nome é {nome} e você tem {calc} anos de idade')
    else:
        print('Ano digitado incorretamente, por favor digite novamente')
    
    
   
    
 

nomeIdade()


#Alan Nicolas de Oliveira | 12011ECP025
#Lucas Albino Martins | 12011ECP022

import threading
import time

read_input = ''
index = 0

def first_lowerCase_to_upperCase(): #TRANSFORMA A PRIMEIRA LETRA MINUSCULA DA ESQUERDA PARA A DIREITA EM MAIUSCULA, IGNORANDO AS QUE JÁ ESTÃO, E OS SÍMBOLOS (SE TIVER)
    global input_string
    global index
    print(input_string)
    while (input_string[index].isupper() or input_string[index] == ' ' or input_string[index].isdigit() or input_string[index].isalnum() == False):
             index = index + 1
    input_string = input_string[:index] + input_string[index].upper() + input_string[index + 1:]
    time.sleep(1)


def read_input():
    global input_string
    input_string = input("Digite a Palavra: ")
    if (len(str(input_string)) > 80):
        input_string = input('Palavra muito grande, digite novamente: ')
    return(input_string)

read_input()
while (str(input_string).isupper() == False and input_string.isdigit() == False): #VERIFICA SE A FRASE DIGITA ESTÁ INTEIRAMENTE NO FORMATO REQUISITADO (MAIUSCULO)
    threading.Thread(first_lowerCase_to_upperCase()).start() #A CADA ITERAÇÃO, É CRIADO UM NOVO THREAD QUE EXECUTA A FUNÇÃO "first_lowerCase_to_upperCase()"
print('Mensagem Resultante: ', input_string)

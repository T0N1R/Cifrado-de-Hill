'''
Antonio Reyes
Cifrado de Hill con matrices 2x2
'''
import math

def abc(diccionario):
    return {' ':0, 'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 
    'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26, 
    '!':27, '?':28}

def cba(diccionario2):
    return {'0':" ", '1':"A", '2':"B", '3':"C", '4':"D", '5':"E", '6':"F", '7':"G", '8':"H", '9':"I", '10':"J",
    '11':"K", '12':"L", '13':"M", '14':"N", '15':"O", '16':"P", '17':"Q", '18':"R", '19':"S", '20':"T", '21':"U", '22':"V", '23':"W",
    '24':"X", '25':"Y", '26':"Z", '27':"!", '28':"?"}

        
def cifrar():
    diccionario = {}
    diccionario = abc(diccionario)

    diccionario2 = {}
    diccionario2 = cba(diccionario2)


    matriztexto = []
    matrizllave = [1,2,3,4]
    cifrado = []
    final = []


    texto = raw_input("Ingrese el texto a cifrar: ")
    llave = raw_input("Ingrese 4 numeros para tener la llave: ")

    if len(texto)%2 != 0:
        texto = texto + " "

    for i in range(0,len(matrizllave)):
        matrizllave[i] = int(llave[i])

    for i in range(0,len(texto)):
        matriztexto.append(diccionario[texto[i]])

    x = 0
    y = 1
    while y<len(texto):
        a = (matrizllave[0] * matriztexto[x]) + (matrizllave[2] * matriztexto[y])
        b = (matrizllave[1] * matriztexto[x]) + (matrizllave[3] * matriztexto[y])

        a = a%29
        b = b%29

        cifrado.append(a)
        cifrado.append(b)

        x = x + 2
        y = y + 2

    for i in range(0,len(cifrado)):
        final.append(diccionario2[str(cifrado[i])])

    #print cifrado

    print final
    

#def solucionar():

def main():
    opcion = 9
    while opcion != 0:
        opcion = input("Ingrese 1 para cifrar y 2 para descifrar: ")
        if opcion == 1:
            cifrar()
    
        if opcion == 2:
            print ("solucionar")


main()


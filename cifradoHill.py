'''
Antonio Reyes
Guillermo Sandoval
Cifrado de Hill con matrices 2xn
'''
import math
import numpy


#Diccionario para convertir el valor ingresado a numeros
def abc(diccionario):
    return {'_':0, 'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 
    'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26, 
    '!':27, '?':28}


#Diccionario para convertir los numeros a letras para descifrar
def cba(diccionario2):
    return {'0':"_", '1':"A", '2':"B", '3':"C", '4':"D", '5':"E", '6':"F", '7':"G", '8':"H", '9':"I", '10':"J",
    '11':"K", '12':"L", '13':"M", '14':"N", '15':"O", '16':"P", '17':"Q", '18':"R", '19':"S", '20':"T", '21':"U", '22':"V", '23':"W",
    '24':"X", '25':"Y", '26':"Z", '27':"!", '28':"?"}

        
def cifrar():
    #Se define un diccionario con un valor para cada caracter en letras mayusculas, para cada caracter un numero
    diccionario = {}
    diccionario = abc(diccionario)

    #Se define el inverso al diccionario1, para cada numero un caracter
    diccionario2 = {}
    diccionario2 = cba(diccionario2)


    matriztexto = []
    matrizllave = [1,2,3,4]
    cifrado = []
    final = []
    enviar = ""

    #Ingresa Matriz y llave
    #Lectura del archivo de texto
    archivo = open("C:\Users\Antonio\Documents\Stuff\Cifrado-de-Hill\cifrado.txt")

    texto = ""

    for line in archivo:
        texto = line.strip()
    archivo.close()
    #texto = raw_input("Ingrese el texto a cifrar: ")
    llave = raw_input("Ingrese 4 numeros para tener la llave (Numeros de 0 a 9 consecutivos): ")

    #convertir len de texto en par agregando un espacio si es necesario.
    if len(texto)%2 != 0:
        texto = texto + "_"

    #crear matriz para llave
    for i in range(0,len(matrizllave)):
        matrizllave[i] = int(llave[i])

    #crear matriz para texto. las letras son numeros
    for i in range(0,len(texto)):
        matriztexto.append(diccionario[texto[i]])

    #multiplicacion de matriz de llave y texto
    x = 0
    y = 1
    while y<len(texto):
        #Se multiplican las llaves de la matriz por una matriz del rexto para encriptarlo
        a = (matrizllave[0] * matriztexto[x]) + (matrizllave[2] * matriztexto[y])
        b = (matrizllave[1] * matriztexto[x]) + (matrizllave[3] * matriztexto[y])

        #Se emplea el modulo 29 por el abecedario
        a = a%29
        b = b%29

        #En una lista escribe el dato y lo adjunta en una cadena
        cifrado.append(a)
        cifrado.append(b)

        x = x + 2
        y = y + 2

    for i in range(0,len(cifrado)):
        final.append(diccionario2[str(cifrado[i])])

    #imprimir cifrado
    for i in range(0,len(final)):
        enviar = enviar + final[i]

    #editar el archivo .txt
    f = open("C:\Users\Antonio\Documents\Stuff\Cifrado-de-Hill\cifrado.txt", "w")
    f.write(enviar)
    print enviar
    

def solucionar():
    #Vuelve a definir el diccionario
    diccionario = {}
    diccionario = abc(diccionario)

    #Vuelve a definir el segundo diccionario para definir los numero a letras
    diccionario2 = {}
    diccionario2 = cba(diccionario2)

    #Se define una matriz de descifrado para el inverso de la matriz de cifrado brindado los numeros que se emplearon para cifrar
    matriztexto = []
    descifrado = []
    final = []
    enviar = ""

    #Ingresa Matriz y llave
    #Lectura del archivo de texto
    archivo = open("C:\Users\Antonio\Documents\Stuff\Cifrado-de-Hill\cifrado.txt")

    cifrado = ""

    for line in archivo:
        cifrado = line.strip()
    archivo.close()

    llave = raw_input("Ingrese la llave utilizada para cifrar: ")

    if len(cifrado)%2 != 0:
        cifrado = cifrado + "_"

    for i in range(0,len(cifrado)):
        matriztexto.append(diccionario[cifrado[i]])
    
    a = int(llave[0])
    b = int(llave[1])
    c = int(llave[2])
    d = int(llave[3])

    #La matriz alterada
    matrizllave = [[a,c],[b,d]]
    llaveAlterada = [[d,c*-1],[b*-1,a]]
    determinante = int(numpy.linalg.det(matrizllave))
    determinante = determinante%29

    #calcular inverso de determinante por modulo inverso
    #https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
    inv = pow(determinante, 27,29)

    llaveAlterada[0][0] = (llaveAlterada[0][0]*inv)%29
    llaveAlterada[1][0] = (llaveAlterada[1][0]*inv)%29
    llaveAlterada[0][1] = (llaveAlterada[0][1]*inv)%29
    llaveAlterada[1][1] = (llaveAlterada[1][1]*inv)%29

    x = 0
    y = 1
    #print matriztexto
    while y<len(cifrado):
        a = (llaveAlterada[0][0] * matriztexto[x]) + (llaveAlterada[0][1] * matriztexto[y])
        b = (llaveAlterada[1][0] * matriztexto[x]) + (llaveAlterada[1][1] * matriztexto[y])

        a = a%29
        b = b%29

        descifrado.append(a)
        descifrado.append(b)

        x = x + 2
        y = y + 2

    for i in range(0,len(cifrado)):
        final.append(diccionario2[str(descifrado[i])])

    #imprimir descifrado
    for i in range(0,len(final)):
        enviar = enviar + final[i]

    #editar el archivo .txt
    f = open("C:\Users\Antonio\Documents\Stuff\Cifrado-de-Hill\cifrado.txt", "w")
    f.write(enviar)
    print enviar



def main():    
    opcion = 9
    while opcion != 0:
        opcion = input("Ingrese 1 para cifrar, 2 para descifrar y 0 para salir: ")
        if opcion == 1:
            cifrar()
    
        if opcion == 2:
            solucionar()


main()

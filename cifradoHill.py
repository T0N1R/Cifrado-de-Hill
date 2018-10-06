'''
Antonio Reyes
Cifrado de Hill con matrices 2x2
'''

def abc(diccionario):
    return {' ':0, 'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 
    'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26, 
    '!':27, '?':28}

def main():
    opcion = 9
    while opcion != 0:
        opcion = input("Ingrese 1 para cifrar y 2 para descifrar: ")
        if opcion == 1:
            cifrar()
    
        if opcion == 2:
            print ("solucionar")

    

def crearMatriz2x2(matriz):
    for i in range(2):
        matriz.append([i]*2)
        

def cifrar():
    diccionario = {}
    diccionario = abc(diccionario)

    matriztexto = []
    matrizllave = []

    crearMatriz2x2(matriztexto)
    crearMatriz2x2(matrizllave)

    texto = raw_input("Ingrese el texto a cifrar")
    llave = raw_input("Ingrese 4 numeros (separados por espacio) para tener la llave: ")

    matrizllave[0][0] = llave[0]
    matrizllave[1][0] = llave[1]

    print (matriztexto)
    print (matrizllave)
    

#def solucionar():


main()


#Programa que imprime este string,ZYWXVUTSRQPONMLKJIHGFEDCBA, hasta imprimir solo A
string = "ZYWXVUTSRQPONMLKJIHGFEDCBA"

#Bucle for para recortar el string desde la izquierda
for i in range(1, 26):
    #Inicializa la variable shortString, que va acortando string desde la izquierta con un espacio
    shortString = string[i:]
    print(shortString)
    print("")
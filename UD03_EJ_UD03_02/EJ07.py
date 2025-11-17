#Programa que lee 100 números no nulos y muestra los negativos

import random

#Inicia la variable contador en 1 para empezar a contar desde ahí y almacenar los números contados en la variable
contador = 1

while contador <= 100:

    num = int(input("Introduce un número positivo o negativo distinto a 0: "))

    if num != 0:

        if num > 0:
            print("Positivo.")
            contador += 1

        elif num < 0:
            print("Negativo.")
            contador += 1

    else:
        print("Número no válido.")
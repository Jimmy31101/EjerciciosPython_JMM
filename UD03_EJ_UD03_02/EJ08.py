#Programa que lee 100 números no nulos y muestra los negativos

import random

#Inicia la variable contador en 1 para empezar a contar desde ahí y almacenar los números contados en la variable
contador = 1
contadorPos = 0
contadorNeg = 0

while contador <= 100:

    num = random.randint(-100, 100)

    for i in range(100):
        if num != 0:

            if num > 0:
                contadorPos += 1
                contador += 1

            elif num < 0:
                contadorNeg += 1
                contador += 1

        else:
            print("Número no válido.")

print("Hay", contadorPos, "números positivos y", contadorNeg, "números negativos")
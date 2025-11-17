#Pide al usuario la altura de la pirámide
altura = int(input("Introduce la altura: "))

#Definición del rango de la pirámide
print("Forma nº1:")
for i in range(altura, 0, - 1):
    #Print de los espacios
    for j in range(altura - i):
        print(" ", end="")

    #Print de los asteriscos
    for k in range(2 * i - 1):
        print("*", end="")
    print()


#Ejemplo clase
print("Forma nº2:")
for i in range(1, altura + 1):
    #Print de los espacios
    for j in range(0, i - 1):
        print(" ", end="")

    #Print de los asteriscos
    for k in range(0, (2 * altura + 1) - (i * 2)):
        print("*", end="")
    print()

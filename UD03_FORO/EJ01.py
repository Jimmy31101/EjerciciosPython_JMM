#Ejercicio figura 1

#Pide al usuario la altura de la pirámide
altura = int(input("Introduce la altura: "))

#Triángulo superior
for i in range(altura + 1):

    #Print de espacios
    for j in range(i, altura):
        print(" ", end=" ")

    #Print de asteriscos
    for j in range(i + 1):
        if i == 0 or j == 0 or j == i:
            print("*", end=" ")

        else:
            print(" ", end=" ")
    print()

#Triángulo inferior
for i in range(altura - 1, - 1, - 1):

    #Print de espacios
    for j in range(i, altura):
        print(" ", end=" ")

    #Print de asteriscos
    for j in range(i + 1):
        if i == 0 or j == 0 or j == i:
            print("*", end=" ")

        else:
            print(" ", end=" ")
    print()
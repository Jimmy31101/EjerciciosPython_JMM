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
        if j == altura - 1 or i + j == altura - 1 or i == j or i == 5:
            print("*", end=" ")

        else:
            print(" ", end=" ")
    print()

print

#Triángulo inferior
for i in range(altura - 1, 0, - 1):

    #Print de espacios
    for j in range(i, altura):
        print(" ", end=" ")

    #Print de asteriscos
    for j in range(i + 1):
        if i == 0 or j == i or j == altura - 1:
            print("*", end=" ")

        else:
            print(" ", end=" ")
    print()
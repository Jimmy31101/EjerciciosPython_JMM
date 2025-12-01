#Ejercicio figura 2

#Pide al usuario la altura de la pirámide
altura = int(input("Introduce la altura: "))

for i in range(1, altura + 1):

    #Print de los 4
    for j in range(1, i + 1):
        if j == 1 or j == i or i == altura:
            print("4", end=" ")

        else:
            print(" ", end=" ")
    print("")
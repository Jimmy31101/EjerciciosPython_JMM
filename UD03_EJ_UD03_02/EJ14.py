#Pide al usuario la altura de la pirámide
altura = int(input("Introduce la altura: "))

#
for i in range(1, altura + 1):
    #Print de los espacios
    for j in range(altura - i):
        print(" ", end="")

    #Print de los asteriscos
    for k in range(1, 2 * i):
        print("*", end="")
    print()
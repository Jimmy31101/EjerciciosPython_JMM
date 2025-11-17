#Pide al usuario la altura de la pirámide
altura = int(input("Introduce la altura: "))

for i in range(1, altura + 1):
    #Print de los asteriscos
    for j in range(1, i + 1):
        print("*", end="")
    print("")
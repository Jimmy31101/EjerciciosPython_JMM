#Ejercicio 1 Diamante Hueco

n = 5

#Print del primer cuadrado
for i in range(n - 1):

    #Print del primer hueco
    for j in range(i, n - 1):
        print(" ", end="")

    #Print del triángulo
    for j in range(i):
        if (j == 0):
            print("*", end="")

        else:
            print(" ", end="")

    #Print del primer triángulo
    for j in range(i + 1):
        if(j == i):
            print("*", end="")

        else:
            print(" ", end="")
    print()

#Segundo triángulo invertido
for i in range(n):

    #Print del segundo hueco
    for j in range(i):
        print(" ", end="")

    for j in range(i, n):
        if(j == i):
            print("*", end="")

        else:
            print(" ", end="")

    #Print del segundo triángulo
    for j in range(i, n - 1):
        if(j == n - 2):
            print("*", end="")

        else:
            print(" ", end="")
    print()
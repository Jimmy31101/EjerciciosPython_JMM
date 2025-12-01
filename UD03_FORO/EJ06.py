#Ejercicio 3 Estructura tipo reja

n = 6

#Print del primer cuadrado
for i in range(n - 1):

    #Print del primer hueco
    for j in range(i, n - 1):
        print(" ", end="")

    #Print del primer triángulo
    for j in range(i):
        if (j == 0 or (i == n // 2 and j % 2 == 0)):
            print("*", end="")

        else:
            print(" ", end="")

    #Print del segundo triángulo
    for j in range(i + 1):
        if(j == i or (i == n // 2 and j % 2 != 0)):
            print("*", end="")

        else:
            print(" ", end="")
    print()
print("*" * (n * 2 - 1))
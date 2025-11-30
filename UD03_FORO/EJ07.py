#Ejercicio 4 Cuadrado con diagonales y borde relleno

n = 7

#Print de las filas
for i in range(n):

    #Print de columnas
    for j in range(n):

        #Print de huecos para las diagonales
        if (j == 5 and i == 4) or (j == 5 and i == 2):
            print(" ", end="")

        #Print de figura con diagonales
        elif j == 0 or j == n - 1 or i == 0 or i == n - 1 or i == j - 1 or i + j == n:
            print("*", end="")

        #Print de huecos
        else:
            print(" ", end="")
    print("\n")
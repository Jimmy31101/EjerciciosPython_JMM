#Ejercicio 4 Cuadrado con diagonales y borde relleno

n = 7

#Print de las filas
for i in range(n):

    for j in range(n):
        if j == 0 or j == n - 1 or i == 0 or i == n - 1 or j == 2 or j == 3 or j == 4 :
            print("*", end="")

        else:
            print(" ", end="")
    print("\n")
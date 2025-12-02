#Ejercicio 7 Triángulo invertido con borde y relleno alternado
"""
******
* * * *
*     *
* * * *
*     *
******
"""

n = 6

#Print con matriz cuadrada
for i in range(n):

    for j in range(n):
        if i== 0 or i == n - 1:
            print("*", end="")

        elif j == 0 or (i % 2 != 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 == 0):
            print("*", end="")

        elif j == n - 1:
            print(" *", end="")

        else:
            print(" ", end="")
    print()
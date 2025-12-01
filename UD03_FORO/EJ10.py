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

#Print de la pirámide invertida
for i in range(n):

    for j in range(i, n):
        print("*", end="")

    for j in range(n, 0, - 1):
        if j > i:
            print("", end="")
        else:
            print("*", end="")
    print()
print("\n")
#Print con matriz cuadrada
for i in range(n):

    for j in range(n):
        if i== 0 or i == n - 1:
            print("*", end="")

        elif j == 0 or j == n - 1 or (i == 1 and j % 2 == 0) or (i == 3 and j % 2 == 0):
            print("*", end="")

        else:
            print(" ", end="")
    print()
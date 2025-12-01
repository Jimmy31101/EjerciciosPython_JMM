#Ejercicio 6 Letra M mayúscula con asteriscos

"""
*     *
**   **
* * * *
*  *  *
*     *
*     *
*     *
"""

n = 7

for i in range(n):

    for j in range(n):
        if j == 0 or j == n - 1:
            print("*", end="")

        elif (i == 4 and j % 2 == 0) or (i == 5 and j % 2 != 0):
            print(" ", end="")

        elif j == i or i + j == n - 1:
            print("*", end="")

        else:
            print(" ", end="")
    print()
#Cruz con borde punteado

"""
. . . . . . .
. * . * . * .
. . * . * . .
* * * * * * *
. . * . * . .
. * . * . * .
. . . . . . .
"""

n = 7

#Print del cuadrado de puntos
for i in range(n):
    #print("·", end=" ")

    #Print de asteriscos dentro del cuadrado de puntos
    for j in range(n):
        if i == n // 2 or (j % 2 != 0 and i % 2 != 0) or (j % 2 == 0 and i == 2 and j != 0 and j != n - 1) or (j % 2 == 0 and i == 4 and j != 0 and j != n - 1):
            print("*", end=" ")

        else:
            print("·", end=" ")
    print()
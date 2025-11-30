#Ejercicio 2 Estrella de ocho puntas

n = 9

#Filas primera figura
for i in range(n):
    if (i == n // 2):
        print("*", end="")

    else:
        print(" ", end="")

    for j in range(n):
        print("*", end="")
    print()
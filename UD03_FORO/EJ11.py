#Ejercicio 8 Rombo Sólido

#Pide al usuario la altura del rombo
altura = int(input("Introduce una altura para la figura:"))

#Primer triángulo
for i in range(altura):

    #Print del primer hueco
    for j in range(altura - i - 1):
        print(" ", end="")

    #Print del primer triángulo
    for k in range(2 * i + 1):
        print("*", end="")
    print()

#Segundo triángulo invertido
for i in range(altura - 2, - 1,  - 1):

    #Print del segundo hueco
    for j in range(altura - i - 1):
        print(" ", end="")

    #Print del segundo triángulo
    for k in range(2 * i + 1):
        print("*", end="")
    print()
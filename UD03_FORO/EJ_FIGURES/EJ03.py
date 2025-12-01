#Ejercicio figura 3

#Pide al usuario la altura de la pirámide
altura = int(input("Introduce la altura: "))

for i in range((altura * 2) + 1):
    for j in range((altura * 2) + 1):
        if i == 0 or i == (altura * 2) or j == 0 or j == (altura * 2) or j % 2 == 0 or i % 2 == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
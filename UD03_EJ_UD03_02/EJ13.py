#Pide al usuario la altura de la pirámide
altura = int(input("Introduce la altura: "))

#La pirámide comienza en 1
num = 1

for i in range(0, altura):
    num = 1

    #Print de los números
    for j in range(0, i + 1):
        print(num, end="")
        num += 1
    print("")
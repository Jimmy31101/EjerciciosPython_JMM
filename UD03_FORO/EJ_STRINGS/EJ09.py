#Leer una cadena y contar cuántas vocales contiene.

#String
word = str(input("Introduce una palabra: "))
counter = 0

for i in word:

    if i == "a" or i == "A":
        counter += 1

    elif i == "e" or i == "E":
        counter += 1

    elif i == "i" or i == "I":
        counter += 1

    elif i == "o" or i == "O":
        counter += 1

    elif i == "u" or i == "U":
        counter += 1

    elif counter == 0:
        print("No se ha encontrado ninguna vocal.")

print("Hay ", counter, " vocales.")
#Construir una nueva cadena con todos los caracteres de la cadena original, pero duplicando cada vocal.

string = "Estamos a martes"
newString = ""
j = - 1

#Bucle para recorrer el string y almacenarlo en el nuevo string
for i in string:
    j += 1

    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
        newString += string[j]

    newString += string[j]

#Muestra por consola el string original
print("Cadena original:", string)

#Muestra por consola el nuevo string
print("Nueva cadena con vocales duplicadas:", newString)
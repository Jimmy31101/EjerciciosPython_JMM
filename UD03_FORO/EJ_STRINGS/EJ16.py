#Leer dos cadenas y concatenarlas manualmente sin usar el operador + en una sola operación (concatenar carácter a carácter con un ciclo).

#Variables
string1 = "Aupa"
string2 = "Atleti"
newString= ""

#Bucles para recorrer los strings caracter por caracter
for i in string1, " ", string2:
    newString += i

#Muestra por consola los strings concatenados
print(newString)
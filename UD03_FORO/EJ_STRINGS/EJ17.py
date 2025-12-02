#Leer una cadena y crear una nueva donde sólo aparezcan los caracteres que se repiten más de una vez.

#Variables
string = "El miercoles nos dan para el pelo"
newString = ""

for i in string:

    if string.count(i) > 1 and i not in newString:
        newString += i

print(newString)
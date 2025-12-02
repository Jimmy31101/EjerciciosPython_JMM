#Reemplazar un carácter por otro recorriendo la cadena y concatenando a una nueva cadena.

#String
string1 = "El miercoles "
string2 = "nos dan para el pelo"
newString = ""

for i in string1:
    newString += i

print(newString + string2)
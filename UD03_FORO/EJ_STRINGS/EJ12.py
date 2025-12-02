#Leer una cadena y construir una nueva cadena con los caracteres en orden inverso.

#String
word = "Un string"
newString = ""

#Opción con un bucle for para hacer un reverse al string
for i in range(len(word)):
    newString = newString + word[-i -1]

#Muestra por consola el string inverso
print(newString)

#Variable reverse donde vamos a guardar el string inverso
reversed = ''.join(reversed(word))

#Muestra por consola el string inverso
print(reversed)
#Dada una cadena, construir una nueva cadena donde cada vocal se reemplaza por un asterisco '*'.

#String
string = "Esto no es un simulacro"

print("Cadena de texto inicial:", string)
#Vocales y caracter a reemplazar
vowels = "aeiouAEIOU"
ast = "*"

#Recorre la variable vowels y las cambia en el string original
for i in vowels:
    string = string.replace(i, ast)

#Muestra el string modificado
print("Cadena de texto con asteriscos:",string)
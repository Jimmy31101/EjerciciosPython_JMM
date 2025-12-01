#Contar cuántas veces aparece un carácter dado en una cadena usando for y un contador.

#Pide al usuario una palabra o frase
phrase = str(input("Introduce una palabra o frase: "))
char = "e"
counter = 0

#Bucle que recorre el string y suma al contador el número de veces que pasa por una letra "e".
for i in phrase:
    if i == char:
        counter += 1

#Muestra en la consola el total de letras "e" encontradas.
print("Hay ", counter, " letras e.")
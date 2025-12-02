#Leer una cadena y contar cuántos caracteres son letras mayúsculas.

word = str(input("Introduce una palabra: "))
counter = 0

#Bucle que recorre el string y suma al contador las mayúsculas encontradas
for i in word:
    if i.isupper():
        counter += 1

#Muestra en consola el total de mayúsculas encontradas
print("Hay ", counter, " mayúsculas.")
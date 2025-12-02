#Leer una cadena y contar cuántos caracteres numéricos ('0' a '9') contiene.

string = "Python 4.1 es la hostia"
letters = 0
numbers = 0

for i in string:

    if i.isalpha():
        letters += 1

    elif i.isdigit():
        numbers += 1

    else:
        pass

print("Números de letras:", letters)
print("Cantidad de números:", numbers)
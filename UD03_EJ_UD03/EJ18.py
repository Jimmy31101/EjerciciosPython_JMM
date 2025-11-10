#Pide un número al usuario
num = int(input("Inserta un número para comprobar si es múltiplo de 10: "))

#Comprueba si es múltiplo de 10 y lo muestra en la consola
if num % 10 == 0:
    print(num, "es múltiplo de 10")

else:
    print(num, "no es múltiplo de 10")
#Calcula el factorial de un número positivo

#Pide el número al usuario
num = int(input("Introduce un número mayor a 0: "))

#Variable result para comenzar a multiplicar en el bucle desde 1
result = 1

#Bucle para calcular el factorial del número definido por el usuario, siempre mayor o igual a 0
if num >= 0:
    for i in range(1, num + 1):
        result *= i

#Excepción en caso de introducir un número no deseado
else:
    print("\nEscribe un número mayor a 0.")

print("\nEl factorial de", num, "es", result)
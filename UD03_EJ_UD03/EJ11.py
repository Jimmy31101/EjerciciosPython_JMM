#Pide al usuario que introduzca dos números
num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce otro número: "))

#Comprueba cuál de los dos números es mayor y los imprime por consola el resultado
if num1 > num2:
    print(num1, "es mayor que", num2,".")

else:
    print(num1, "es menor que", num2,".")
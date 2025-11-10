#Pide al usuario dos números
num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce otro número: "))

#Comprueba cuál de los dos números es mayor o si son iguales, y los imprime por consola el resultado
if num1 == num2:
    print("Los números son iguales.")

elif num1 > num2:
    print(num1, "es mayor que", num2)

elif num1 < num2:
    print(num2, "es mayor que", num1)
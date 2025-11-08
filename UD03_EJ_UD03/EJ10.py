#Leemos las variables
num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce otro número:"))

#Realizamos los cálculos de suma, resta, producto y división
if num1 & num2 > 0:
    suma = num1 + num2
    resta = num1 - num2
    producto = num1 * num2
    division = num1 / num2

    print("Suma: ", suma,
          "\nResta: ", resta,
          "\nProducto: ", producto,
          "\nDivisión: ", division)

else:
    print("Introduce un número mayor a 0.")
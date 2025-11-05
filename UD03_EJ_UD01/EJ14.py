num1 = int(input("Introduce un número mayor que 0: "))

num2 = int(input("Introduce otro número mayor que 0: "))

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
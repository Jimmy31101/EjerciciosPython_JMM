#Pide al usuario tres números
num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce el segundo número: "))
num3 = int(input("Introduce el tercer número: "))

#Comprueba cuál de los tres números es mayor o si son iguales, y los imprime por consola el resultado
if num1 > num2:

    if num1 == num3:
        print(num3, "=", num1, ">", num2)

    else:
        if num1 > num3:

            if num2 > num3:
                print(num1, ">", num2, ">", num3)

            else:
                if num2 == num3:
                    print(num1, ">", num3, "=", num2)

                else:
                    print(num1, ">", num3, ">", num2)
        else:
            print(num3, ">", num1, ">", num2)

else:
    if num1 == num2:

        if num2 > num3:
            print(num2, "=", num1, ">", num3)

        else:
            if num2 == num3:
                print(num3, "=", num2, "=", num1)

            else:
                print(num3, ">", num2, "=", num1)

    else:
        if num2 > num3:

            if num1 > num3:
                print(num2, ">", num1, ">", num3)

            else:
                if num1 == num3:
                    print(num2, ">", num3, "=", num1)

                else:
                    print(num2, ">", num3, ">", num1)

        else:
            if num2 == num3:
                print(num2, "=", num3, ">", num1)

            else:
                print(num3, ">", num2, ">", num1)
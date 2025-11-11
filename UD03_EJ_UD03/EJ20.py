#Pide al usuario que introduzca una nota entre 0 y 10
num = float(input("Introduce una nota: "))

#Switch donde comprobamos en que rango de notas se encuentra la nota introducida e imprime por consola el resultado
match num:
    case num if  0 <= num < 3:
        print("Muy deficiente.")

    case num if  3 <= num < 5:
        print("Insuficiente.")

    case num if  5 <= num < 6:
        print("Suficiente.")

    case num if  6 <= num < 7:
        print("Bien.")

    case num if  7 <= num < 9:
        print("Notable.")

    case num if  9 <= num <= 10:
        print("Sobresaliente.")
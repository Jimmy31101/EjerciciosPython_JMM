num = float(input("Introduce una nota: "))

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
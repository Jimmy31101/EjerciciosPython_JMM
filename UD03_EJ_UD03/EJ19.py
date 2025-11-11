#Inicializamos el saldo inicial
saldoInicial = 1000

#Muestra un mensaje de bienvenida al cliente y el menú
print("\nBienvenido a Cajasur")

#Bucle del menú interactivo
while (True):
    print("""\nElige una de las opciones para continuar:
      1. Ingresar dinero en cuenta
      2. Retirar dinero de la cuenta
      3. Salir""")

    print("\nSaldo disponible:", saldoInicial, "\n")

    opcion = int(input())

    if opcion == 1:
        print("""¿Cuánto dinero desea ingresar?: """)

        saldoMonto = int(input())
        saldoInicial += saldoMonto

    elif opcion == 2:
        print("¿Cuánto dinero desea retirar?: ")

        saldoRetiro = int(input())
        saldoInicial -= saldoRetiro

    elif opcion == 3:
        print("¡Hasta la próxima!, ha sido un placer ayudarte")
        break

    else:
        print("Comando desconocido, vuelve a intentarlo")
#Inicializamos el total de la venta
totalVenta = float(input("Introduce el total de la venta: "))
ventaFinal = 0

#Muestra un mensaje de bienvenida al cliente y el menú
print("\nBienvenido a Kawanda")

#Bucle del menú interactivo
while (True):
    print("""\nElige una de las opciones para continuar:
      1. Pago en efectivo
      2. Pago con tarjeta
      3. Salir""")

    print("\nTotal de la venta sin descuento:", totalVenta, "\n")

    opcion = int(input())

    if opcion == 1:
        totalVenta *= 0.05
        ventaFinal -= totalVenta
        print("""Total de la compra, descuento 5%: """, ventaFinal)

    elif opcion == 2:
        totalVenta *= 0.03
        ventaFinal -= totalVenta
        print("""Total de la compra, descuento 3%: """, ventaFinal)

    elif opcion == 3:
        print("¡Hasta la próxima!, gracias por comprar en Kawanda")
        break

    else:
        print("Comando desconocido, vuelve a intentarlo")
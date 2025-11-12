#Inicializamos el total de la venta
totalVenta = float(input("Introduce el total de la venta: "))
ventaFinal = 0
precioFinal = 0

#Muestra un mensaje de bienvenida al cliente y el menú
print("\nBienvenido a Kawanda")

#Menú interactivo
while (True):
    print("""\nElige una de las opciones para continuar:
      1. Pago en efectivo
      2. Pago con tarjeta
      3. Salir""")

    print("\nTotal de la venta sin descuento:", totalVenta, "\n")

    option = int(input())

    if option == 1:
        ventaFinal = (totalVenta * 5) / 100
        precioFinal = totalVenta - ventaFinal
        print("""\nTotal de la compra, descuento 5%: """, precioFinal)

    elif option == 2:
        ventaFinal = (totalVenta * 3) / 100
        precioFinal = totalVenta - ventaFinal
        print("""\nTotal de la compra, descuento 3%: """, precioFinal)

    elif option == 3:
        print("\n¡Hasta la próxima!, gracias por comprar en Kawanda")
        break

    else:
        print("\nComando desconocido, vuelve a intentarlo")
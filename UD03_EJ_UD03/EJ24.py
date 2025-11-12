#Inicializamos el total de la venta
totalVenta = float(input("Introduce el total de la venta: "))
diaSemana = str(input("Y el día de la semana: "))
ventaFinal = 0
precioFinal = 0

if diaSemana.lower() == "martes" or diaSemana.lower() == "jueves":
    ventaFinal = (totalVenta * 15) / 100
    precioFinal = totalVenta - ventaFinal
    print("""\nTotal a pagar con un descuento del 15%: """, precioFinal)

else:
    print("""\nTotal a pagar: """, totalVenta)
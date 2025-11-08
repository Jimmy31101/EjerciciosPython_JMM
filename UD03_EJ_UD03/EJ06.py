precioVenta = int(input("Introduce el precio de venta: "))

precioProd = int(input("Introduce el precio del producto: "))

descuento = 100 - (100 * precioVenta) / precioProd

print("El descuento es del: ", descuento, "%")
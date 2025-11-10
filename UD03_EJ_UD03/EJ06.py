#Pide al usuario el precio de venta y el precio del producto
precioVenta = int(input("Introduce el precio de venta: "))
precioProd = int(input("Introduce el precio del producto: "))

#Cálculo del descuento al precio del producto
descuento = 100 - (100 * precioVenta) / precioProd

#Imprime por consola el descueto
print("El descuento es del: ", descuento, "%")
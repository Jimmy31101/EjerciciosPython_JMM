#Escribe un programa que calcule la suma y el producto de los 10 primeros números naturales

#Bucle dónde cuenta los 10 primero números naturales
for i in range(1, (10 + 1)):
    num = i
    suma = num + i
    prod = num * i
    #print(i,suma, prod)

print("Suma de los 10 primeros números naturales", suma)
print("Producto de los 10 primeros números naturales", prod)
#Programa para cálcular la potencia de un número sin usar el operador(^)

#Pide al usuario el número y el exponente
num = int(input("Introduce un número:"))
exp = int(input("Introduce un exponente:"))
resultado = 1

#Calcula la potencia multiplicando num tantas veces sea exp
for i in range(1, exp + 1):
    resultado *= num

#Muestra el resultado en la consola
print(resultado)
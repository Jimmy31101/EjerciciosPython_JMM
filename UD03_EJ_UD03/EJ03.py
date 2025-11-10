#Pide al usuario el valor de la variable lado
lado = int(input("Introduce el lado del cuadrado: "))

#Condición para que lado sea mayor que cero para calcular el área del cuadrado
if lado > 0:
    area = (lado * lado)

#Imprime por consola el largo del lado y el resultado del área
print("El área del cuadrado con lado ", lado, " es: ", area)
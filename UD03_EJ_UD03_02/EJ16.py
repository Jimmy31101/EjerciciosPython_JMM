#Programa que pide al usuario una nota y muestra el número de sobresalientes

#Pide al usuario la nota
nota = float(input("Introduce una nota entre 0 y 10: "))
contador = 0

#Comprobación de la nota entre 0 y 10
if 0 <= nota <= 10:

    #Condición para sumar al contador y mostrar el número de sobresalientes iguales a 10
    if nota == 10:
        contador += 1
    print("Hay", contador, "sobresalientes.")

else:
    print("Nota introducida no válida.")
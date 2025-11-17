#Programa que suma los números pares e impares comprendidos entre 100 y 200, sumándolos por separado

#Inicializa las variables sumaPar y sumaImpar
sumaPar = 0
sumaImpar = 0

#Delimita el rango en el bucle
for i in range(100, 200):

    #Comprobación si es par o impar
    if i % 2 == 0:
        sumaPar += 1

    else:
        sumaImpar += 1

print("Hay", sumaPar, "números pares."
      "\nHay", sumaImpar, "números impares.")
sumaPar = 0
sumaImpar = 0

for i in range(100, 200):

    if i % 2 == 0:
        sumaPar += 1

    else:
        sumaImpar += 1

print("Hay", sumaPar, "números pares."
      "\nHay", sumaImpar, "números impares.")
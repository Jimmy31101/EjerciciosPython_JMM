aux = 1
contador500 = 0
contador200 = 0
contador100 = 0
contador50 = 0
contador20 = 0
contador10 = 0
contador5 = 0
bandera = 0
cantidad = int(input("Introduce una cantidad que sea múltiplo de 5: "))

while bandera != 1:

    if cantidad == aux * 5:

        while bandera != 1:

            if cantidad >= 500:
                cantidad -= 500
                contador500 += 1

            elif cantidad >= 200:
                cantidad -= 200
                contador200 += 1

            elif cantidad >= 100:
                cantidad -= 100
                contador100 += 1

            elif cantidad >= 50:
                cantidad -= 50
                contador50 += 1

            elif cantidad >= 20:
                cantidad -= 20
                contador20 += 1

            elif cantidad >= 10:
                cantidad -= 10
                contador10 += 1

            elif cantidad >= 5:
                contador5 -= 5
                contador5 += 1

            elif cantidad < 5 & cantidad > 0:
                print("No se puede hacer.")
                contador500 = 0
                contador200 = 0
                contador100 = 0
                contador50 = 0
                contador20 = 0
                contador10 = 0
                contador5 = 0
                bandera = 1

            else:
                bandera = 1

    else:
        if cantidad > aux * 5:
            aux += 1

        else:
            bandera = 1

print("Billetes de 500:", contador500,
      "\nBilletes de 200:", contador200,
      "\nBilletes de 100:", contador100,
      "\nBilletes de 50:", contador50,
      "\nBilletes de 20:", contador20,
      "\nBilletes de 10:", contador10,
      "\nBilletes de 5:", contador5)
#Inicializa las variables
tarifaNormal = float(input("Introduce la tarifa estándar(€): "))
totalHoras = float(input("Introduce las horas trabajadas: "))
pagar = 0
bolsillo = 0

#Condiciones para realizar los pagos dependiendo de la tarifa y las horas trabajadas
if totalHoras <= 35:
    pagar = pagar + (totalHoras * tarifaNormal)
    #print(pagar)
else:
    pagar = pagar + (totalHoras * tarifaNormal)
    totalHoras = totalHoras - 35
    pagar = pagar + (totalHoras * (tarifaNormal * 1.5))

if pagar < 500:
    bolsillo = pagar

else:
    bolsillo = bolsillo + 500
    pagar = pagar - 500

if pagar <= 400:
    bolsillo = bolsillo + (pagar - (25 / 100))

else:
    bolsillo = bolsillo + (400 - (25 / 100))
    pagar = pagar - 400
    bolsillo = bolsillo + (pagar - (45 / 100))

print(bolsillo, "€")
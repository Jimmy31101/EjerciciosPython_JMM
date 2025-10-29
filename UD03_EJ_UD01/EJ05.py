radio = int(input("Introduce la longitud del radio: "))

diametro = radio * 2

longitud = 3.1416 * diametro

area = 3.1416 * radio ** 2

volumen = (4 * 3.1416 * radio ** 3) / 3

print("Circunferencia con radio = ", radio,
      "\nDiámetro de la circunferencia = ", diametro,
      "\nLongitud de la circunferencia = ", longitud,
      "\nÁrea de la circunferencia = ", area,
      "\nVolumen de la circunferencia = ", volumen)
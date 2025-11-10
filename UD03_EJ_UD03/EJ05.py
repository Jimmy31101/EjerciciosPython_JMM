#Pide al usuario el valor de la variable radio
radio = int(input("Introduce la longitud del radio: "))

#Cálculos del diámetro, longitud, área y volumen de la figura geométrica
diametro = radio * 2
longitud = 3.1416 * diametro
area = 3.1416 * radio ** 2
volumen = (4 * 3.1416 * radio ** 3) / 3

#Imprime por consola el resultado de los cálculos
print("Circunferencia con radio = ", radio,
      "\nDiámetro de la circunferencia = ", diametro,
      "\nLongitud de la circunferencia = ", longitud,
      "\nÁrea de la circunferencia = ", area,
      "\nVolumen de la circunferencia = ", volumen)
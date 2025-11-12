#Pide al usuario que ingrese el nombre del postulante y la facultad donde va a estudiar
name = str(input("Escriba el nombre del postulante: "))

#Menú interactivo para seleccionar la universidad
while True:
    print("""\nElija una de las siguientes universidades:
          1. Ing. de Sistemas
          2. Derecho
          3. Ing. Naviera
          4. Ing. Pesquera
          5. Contabilidad
          6. Administración
          7. Salir""")

    option = int(input())

    #Switch dónde realiza el cálculo del pago total para cada caso
    match option:
        case 1:
            importe = 350
            mensualidad = 650
            IGV = 18 / 100

            importeIGV = (importe + mensualidad) * IGV
            importeTotal = importe + mensualidad + importeIGV
            print("""\nPara Ing. de Sistemas el importe total es de :""", importeTotal,"€")

        case 2:
            importe = 300
            mensualidad = 550
            IGV = 18 / 100

            importeIGV = (importe + mensualidad) * IGV
            importeTotal = importe + mensualidad + importeIGV
            print("""\nPara Derecho el importe total es de :""", importeTotal,"€")

        case 3:
            importe = 300
            mensualidad = 500
            IGV = 18 / 100

            importeIGV = (importe + mensualidad) * IGV
            importeTotal = importe + mensualidad + importeIGV
            print("""\nPara Ing. Naviera el importe total es de :""", importeTotal,"€")

        case 4:
            importe = 310
            mensualidad = 460
            IGV = 18 / 100

            importeIGV = (importe + mensualidad) * IGV
            importeTotal = importe + mensualidad + importeIGV
            print("""\nPara Ing. Pesquera el importe total es de :""", importeTotal,"€")

        case 5:
            importe = 280
            mensualidad = 490
            IGV = 18 / 100

            importeIGV = (importe + mensualidad) * IGV
            importeTotal = importe + mensualidad + importeIGV
            print("""\nPara Contabilidad el importe total es de :""", importeTotal,"€")

        case 6:
            importe = 360
            mensualidad = 520
            IGV = 18 / 100

            importeIGV = (importe + mensualidad) * IGV
            importeTotal = importe + mensualidad + importeIGV
            print("""\nPara Administración el importe total es de :""", importeTotal,"€")

        case 7:
            break

        case _:
            print("Opción seleccionada no válida, inténtelo de nuevo.")
nota = float(input("Introduce una nota entre 0 y 10: "))
contador = 0

if 0 <= nota <= 10:
    if nota == 10:
        contador += 1
    print("Hay", contador, "sobresalientes.")

else:
    print("Nota introducida no válida.")
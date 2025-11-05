contador = 1
contador_pos = 0
contador_neg = 0

while contador <= 3:

    num = int(input("Introduce un número positivo o negativo distinto a 0: "))

    if num != 0:

        if num > 0:
            contador += 1
            contador_pos += 1

        elif num < 0:
            contador += 1
            contador_neg += 1

    else:
        print("Número no válido.")

print("Hay", contador, "números.")
print("Hay", contador_pos, "números positivos.")
print("Hay", contador_neg, "números negativos.")
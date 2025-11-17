num = int(input("Introduce un número positivo o negativo distinto a 0: "))
contador = 0
contador_pos = 0
contador_neg = 0

if num != 0:

    while contador < 3:

        if num > 0:
            num = int(input("Introduce un número positivo o negativo distinto a 0: "))
            contador += 1
            contador_pos += 1

        else:
            num = int(input("Introduce un número positivo o negativo distinto a 0: "))
            contador += 1
            contador_neg += 1

print("Hay", contador, "números.")
print("Hay", contador_pos, "números positivos.")
print("Hay", contador_neg, "números negativos.")
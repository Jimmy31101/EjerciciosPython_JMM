num = int(input("Introduce un número mayor a 0: "))

result = 1

if num >= 0:
    for i in range(1, num + 1):
        result *= i

else:
    print("\nEscribe un número mayor a 0.")

print("\nEl factorial de", num, "es", result)
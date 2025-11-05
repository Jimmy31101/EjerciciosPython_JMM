num = int(input("Introduce un número mayor a 0: "))

result = 1

if num > 0:
    for i in range(1, num + 1):
        result *= i
    print(result)

else:
    print("Escribe un número mayor a 0.")
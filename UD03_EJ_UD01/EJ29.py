import random
randnum = random.randint(1, 100)

print("Bienvenido a Adivina el Número \n tienes 7 intentos para adivinar el número que piensa el ordenador.")
num = int(input("\nInserta un número entre 1 y 100: "))

intentos = 0

match num:
    case 1:
        num
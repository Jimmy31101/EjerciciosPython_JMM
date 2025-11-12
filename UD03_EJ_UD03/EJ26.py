#Importa la clase math
import random

#Menú interactivo del juego
while True:
    print("""\nElija una de las siguientes universidades:
          1. Tirar dados
          2. Salir""")

    option = int(input())

    match option:
        case 1:
            #Inicia las variables dice
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            dice3 = random.randint(1, 6)

            if dice1 and dice2 and dice3 == 6:
                print("\nExcelente!")

            elif (dice1 and dice2 == 6) or (dice2 and dice3 == 6) or (dice1 and dice3 == 6):
                print("\nMuy bien!")

            elif dice1 or dice2 or dice3 == 6:
                print("\nRegular")

            else:
                print("\nPésimo")

        case 2:
            break

        case _:
            print("Opción incorrecta, inténtalo de nuevo.")
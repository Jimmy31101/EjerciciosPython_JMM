#Verificar si un carácter específico está en la cadena con un ciclo y comparaciones.

#String y caractér a encontrar
word = "El miercoles nos dan para el pelo"
char = "o"
found = False

#Bucle para recorrer el string
for i in word:
    if i == char:
        found = True

#Condición para mostrar si el string contiene la letra "o".
if found:
    print("La letra 'o' está dentro del string.")

else:
    print("La letra 'o' no está dentro del string.")
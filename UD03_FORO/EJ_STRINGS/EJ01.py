#Leer una cadena desde teclado y mostrarla carácter por carácter usando un ciclo for y el índice.

word = str(input("Introduce una frase para mostrar sus caractéres: "))

for i in word:
    print(word.index(i), i)
    #print(f"Carácter {i}: {word[i]}")
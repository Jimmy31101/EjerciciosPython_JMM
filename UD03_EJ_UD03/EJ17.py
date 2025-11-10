#Pide al usuario el nombre de usuario y la contraseña
username = input("Introduce tu nombre de usuario: ")
password = input("Introduce tu nombre de contraseña: ")

#Comprueba si el nombre de usuario y contraseña son correctos
if username == "admin" and password == "password":
    print("Login correcto")

else:
    print("Usuario o contraseña incorrectos")
#Importa la librería de fechas
from datetime import datetime, time, timedelta

#Hora fijada
horaInicial = time(23, 59, 00)

#Inicializa la variable
fechaActual = datetime.now().date()
fechaFinal = datetime.combine(fechaActual, horaInicial)

#Añade 1 segundo
segundosAdd = 1
nuevaFecha = fechaFinal + timedelta(seconds=segundosAdd)
nuevaHora = nuevaFecha.time()

#Imprime por consola la fecha actual en horas, minutos y segundos, y la fecha con el segundo extra
print("Hora actual:", horaInicial)
print("\nHora final:", nuevaHora)
# 01 - Importo librerias necesarias:
import scrapy
from datetime import datetime

# 02-  Configuro el la fecha actual:
hora = datetime.now().time()
fecha = datetime.now().today()

#03- Formato correcto para la fecha y hora:
fHoraMinuto = "%H:%M"
fDiaMesAño = "%d-%m-%Y"

horaActual = hora.strftime(fHoraMinuto)
fechaActual = fecha.strftime(fDiaMesAño)

# prueba de resultado:
print(f'''
La fecha actual es: {fechaActual}
La hora actual es: {horaActual}''')

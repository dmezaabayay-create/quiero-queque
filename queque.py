import os
import time
from datetime import datetime

def limpiar_pantalla():
    # Limpia la consola según el sistema operativo (Windows o Linux/Mac)
    os.system('cls' if os.name == 'nt' else 'clear')

try:
    limpiar_pantalla()
    while True:
        ahora = datetime.now()
        fecha = ahora.strftime("%d/%m/%Y")
        hora = ahora.strftime("%H:%M:%S")

        # Limpiamos la pantalla en cada iteración para asegurar compatibilidad
        limpiar_pantalla()
        print(f"--- RELOJ DIGITAL ---\nFecha: {fecha}\nHora:  {hora}")
        
        time.sleep(1)

except KeyboardInterrupt:
    print("\n\nPrograma finalizado correctamente.")
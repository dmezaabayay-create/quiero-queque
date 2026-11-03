import time
from datetime import datetime

try:
    # Mostramos la fecha inicial arriba
    fecha = datetime.now().strftime("%d/%m/%Y")
    print(f"Fecha Actual: {fecha}")
    
    while True:
        ahora = datetime.now().strftime("%H:%M:%S")
        
      
        print(f"\rHora Actual: {ahora}", end="", flush=True)
        
        time.sleep(1)

except KeyboardInterrupt:
    print("\n\nPrograma interrumpido por el usuario.")

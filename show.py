# Importación de librerias
import webbrowser
import os
import time




#Mostrar imagenes
def show_pics(html, nombre):
    """
    Se abrirá un navegador con la información del pokemon y una imagen.

    Args:
        html: 
        nombre: Nombre de pokemon

    Returns:

    """
    with open(f'{nombre}.html','w') as f:
        f.write(html)
    print('|Se mostrará la tarjeta POKEMON en tu navegador...|')
    time.sleep(2)
    webbrowser.open(f'{nombre}.html')
    #time.sleep(5)
    #os.remove(f'{nombre}.html')
    
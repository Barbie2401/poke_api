
import webbrowser
import os
import time


def show_pics(html, nombre):
    with open(f'{nombre}.html','w') as f:
        f.write(html)
    print('|Se mostrará la tarjeta POKEMON en tu navegador...|')
    time.sleep(2)
    webbrowser.open(f'{nombre}.html')
    #time.sleep(5)
    #os.remove(f'{nombre}.html')
    
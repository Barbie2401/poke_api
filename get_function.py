######## Funciones ########
import html_data

#Funciones que se llamarán en el codigo:


#De varias listas, la transforma a una lista plana que contiene todos los elementos de las sublistas anidadas.
def flatten(t):
    """
    Esta función toma una lista de listas 
    y devuelve una lista plana que contiene todos los 
    elementos de las sublistas anidadas.
    
    Args:
        t: lista

    Return:
        Lista plana que contiene todos los elementos de las sublistas anidadas.


    """
    return [item for sublist in t for item in sublist]




#Traductor de lista ingles a español   
def en_to_es_list(l):
    """ Traduce los elementos de una lista de ingles a español

    Args:
        l: lista en ingles
    Resturn: 
        Lista en español
    """
    translated = []

    #recorrer cada elemento de la lista original
    for to_translate in l:
        # agrega el valor traducido a una nueva lista llamada translated
        translated.append(html_data.tipos_es[to_translate])
    #Restorna la lista con los elementos traducidos
    return translated



#Tipo de daño del pokemon
def render_pokemon_damage(list_es, list_en):
    """
    Función que entrega el tipo de daño del pokemon

    Args:
        list_es: Lista en español
        list_en: Lista en ingles
        
    Resturn: 
        Entrega el tipo de daño del pokemon
    """

    index = 0
    # print(list_es, list_en)
    if not list_en or not list_es:
        return ''
    else:
        types_to_render = []
        for i, damage in enumerate(list_es):
            types_to_render.append(f'''<span class="label {list_en[i]}">{damage}</span>''')
            index += 1
        return ' '.join(types_to_render)

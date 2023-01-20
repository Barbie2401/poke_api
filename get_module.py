import requests
import json

#De un url crea un diccionario
def get_info(url):
    """
    Toma una URL como argumento y utiliza el módulo requests para hacer una solicitud GET a esa URL.
     Luego, utiliza el método '.text' para obtener el contenido de la respuesta como una cadena de 
     texto y la pasa a json.loads() para convertirla en un diccionario de Python.
    
    Arg:
        url: Inserte una url
    
    Returns:
        Diccionario de Python
        
    """
    return json.loads(requests.get(url).text)




if __name__ == '__main__':
    url = f'https://pokeapi.co/api/v2/pokemon/charmander'
    print(get_info(url))

   


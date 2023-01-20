import requests
import json


# Buscar el pokemon por el nombre
def fetch_pokemon(name):
    """
    Buscar el pokemon con el nombre que ingreso el usuario

    Args: 
        name: Nombre de pokemon ingresado por el usuario

    Returns:
        Diccionario con la información de el pokemon
    """

    dicc={}
    for key in ["pokemon", "pokemon-species"]:
        url = f"https://pokeapi.co/api/v2/{key}/{name}" 
        response = requests.request("GET", url) 
        dicc[key] = json.loads(response.text)
    # Retorna diccionario
    return dicc

if __name__ == '__main__':
    name = 'pikachu' 
    print(fetch_pokemon(name))



# Buscar pokemon por el tipo de pokemon
def fetch_pokemon_type(pokemon_type):
    """
    Buscar pokemon por el tipo de pokemon

    Args:
        pokemon_type: Tipo de pokemon

    Returns: 
        Diccionario con la descripción del tipo de pokemon
    """
    type_description_dic = {}
    for type_1 in pokemon_type:
        url=f"https://pokeapi.co/api/v2/type/{type_1}"
        response = requests.request("GET", url)
        type_description_dic = json.loads(response.text)
    # Diccionario con la descripción del tipo de pokemon
    return type_description_dic
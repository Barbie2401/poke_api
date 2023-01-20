import requests
import json



#asdasd
def fetch_pokemon(name):
    dicc={}
    for key in ["pokemon", "pokemon-species"]:
        url = f"https://pokeapi.co/api/v2/{key}/{name}" 
        response = requests.request("GET", url) 
        dicc[key] = json.loads(response.text)
    return dicc

if __name__ == '__main__':
    name = 'pikachu' 
    print(fetch_pokemon(name))

def fetch_pokemon_type(pokemon_type):
    type_description_dic = {}
    for type_1 in pokemon_type:
        url=f"https://pokeapi.co/api/v2/type/{type_1}"
        response = requests.request("GET", url)
        type_description_dic = json.loads(response.text)
    return type_description_dic
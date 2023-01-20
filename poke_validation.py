# Abrir archivo que contiene los nombres de pokemones
with open("pokemon_list.txt", "r") as f:
    pokemon_lista = f.readlines()



# Crea una lista con los nombre de los pokemones
pokemon_lista = [elemento.strip('\n') for elemento in pokemon_lista]
# import data as d
# print(pokemon_lista)



# Valida si el nombre escrito por el usuario se encuentra dentro de la lista de nom,bre de pokemones.
def validate(name, p_l = pokemon_lista, mensaje = "\nError, Pokémon no válido.\nIngrese un nombre de Pokémon válido: "):
    """
    Validación de pokemon
    
    Args:
        name: Nombre de pokemon

    Return:
        Valida si el nombre escrito por el usuario se encuentra dentro de la lista de nom,bre de pokemones.

    """
    
    while True:
        #Caso especial    
        if name =='codigo-cero':
            name = 'type-null'
        #Si está en la lista
        if name not in p_l:
            name = input(mensaje).lower()
        #Si está en la lista
        else:    
            return name


if __name__ == '__main__':
    # name = 'codigo-cero'
    while True:
        name = input("Ingrese nombre de pokemon: ")
        print(validate(name))

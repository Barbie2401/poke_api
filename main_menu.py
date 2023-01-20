# Importación de librerias
import random

# Llamado de modulos
from poke_validation import validate
import utils as u
import html_data
from show import show_pics
from get_function import flatten, en_to_es_list, render_pokemon_damage
from get_data import fetch_pokemon, fetch_pokemon_type

# Loop para presentar opciones
while True: #Creamos un bucle
    # Obtener los datos de entrada
    opcion = input (u.mensaje_opcion)
    opcion = int(validate(opcion, ['0','1',], mensaje = u.validacion_opcion))
    
    if opcion == 1:
        pokemon_name = input(u.mensaje_pokedex).lower() #lower permite colocar en minusculas las letras
        pokemon_name = validate(pokemon_name)

        # Diccionarios para acceder a contenidos de las urls
        dicc = fetch_pokemon(pokemon_name) 

        # Datos de pokemon
        nombre_pokemon = dicc["pokemon"]['name'].capitalize()
        id_pokemon =dicc["pokemon"]['id']
        estadist_pokemon = dicc["pokemon"]['stats']
        img_pokemon = dicc['pokemon']['sprites']['front_default'] 
        etapa_prev = dicc['pokemon-species']['evolves_from_species']
        etapa_prev_v =None
        peso_pokemon = dicc["pokemon"]['weight']
        alt_pokemon = dicc["pokemon"]['height']
        ind_esp_bebe = dicc["pokemon-species"]['is_baby']
        ind_esp_legen = dicc["pokemon-species"]['is_legendary']
        ind_esp_mit = dicc["pokemon-species"]['is_mythical']
        ind_especial = ' '

       # Busqueda de la etapa previa. Sino tiene, escribe No tiene
        if etapa_prev == None:
            etapa_prev = 'Sin información'
        else:
            if etapa_prev is not None:
                etapa_prev = dicc['pokemon-species']['evolves_from_species']['name']  

        # Busqueda de indicadores especiales(Bebé, Legendario, Mitico)
        if ind_esp_bebe is True:
            ind_esp_bebe = 'Bebé'
            ind_especial = ind_esp_bebe

        if ind_esp_legen is True:
            ind_esp_legen = 'Legendario'   
            ind_especial = ind_esp_legen
        
        if ind_esp_mit is True:
            ind_esp_mit = 'Mítico'   
            ind_especial = ind_esp_mit
        
        else:
            if ind_esp_bebe and ind_esp_legen and ind_esp_mit is False:
                ind_especial = 'No tiene'

        # Tipo_pokemon
        html_body= f"""
            <img src="https://raw.githubusercontent.com/PokeAPI/media/master/logo/pokeapi_256.png" width="150" height="60">
            <center>
                <h5>Etapa previa: {etapa_prev}</h5>
            </center>
            <h1>#{id_pokemon} {nombre_pokemon}</h1>
            <hr>
            <img src="{img_pokemon}" width="150" height="150">
            <hr>
            <div class="container">
                <center>
                    <h4>Peso:{peso_pokemon} | Altura:{alt_pokemon}</h4>
                </center>
            <hr>
            <center>
                <h4>Indicador especial: {ind_especial} </h4>
            </center>
            <hr>
            <h2>Estadísticas</h2>
            <table> 
                <tr>"""
                    
        # Extraer información estadistica del pokemon
        for st in estadist_pokemon:
            estadis_pk_es = html_data.dicc_estadistic[st['stat']['name']]

            html_body +=f"""<td><h5>{estadis_pk_es}:\n{st['base_stat']}</h5></td>"""
    
        html_body += f"""
                </tr> 
            </table>
            <h3><b>Tipo </b></h3>"""
 
        # Tipos de pokemon. ej:agua, roca, etc
        tipos_lista_pk=dicc["pokemon"]['types']
        pokemon_type_en = []

        for name_type in tipos_lista_pk:
            # print (name_type['type']['name'])
            pokemon_type_en.append(name_type['type']['name'])
            # traduccion de tipo de pokemon a travezs de lista html_data
            pokemon_tipo_es = []
            pokemon_tipo_es = html_data.tipos_es[name_type['type']['name']]
            pokemon_type = name_type['type']['name']
            html_body +=f'<span class="label {pokemon_type}">{pokemon_tipo_es}</span>'

        # Lista con descripciones en español del pokemon elegido    
        lista_descripcion=[]
        for descripcion in dicc['pokemon-species']['flavor_text_entries']:
            if descripcion['language']['name']=='es':
                # print(descripcion['flavor_text'])
                lista_descripcion.append(descripcion['flavor_text'])
        
        # Se elige de manera random una descripción al azar
        descrip=random.choice(lista_descripcion).replace("\n"," ") 

        html_body +=f'''<p>{descrip}</p>'''

        # Diccionario con informacion de los tipos de pokemon
        type_description_dic = fetch_pokemon_type(pokemon_type_en)
    
        # Extraccion damage relations
        demage_relations = type_description_dic['damage_relations']

        # Listas vacias que se llenarán con sus respectiva información
        super_efectivo_contra = []
        debil_contra = []
        resistente_contra = []
        poco_eficaz_contra = []
        inmune_contra = []
        inneficaz_contra = []

        # Extraer el nombre del tipo de pokemon según lista correspondiente (EN INGLES)
        super_efectivo_contra.append([dd['name'] for dd in demage_relations['double_damage_from']])
        debil_contra.append([dd['name'] for dd in demage_relations['double_damage_to']])
        resistente_contra.append([dd['name'] for dd in demage_relations['half_damage_from']])
        poco_eficaz_contra.append([dd['name'] for dd in demage_relations['half_damage_to']])
        inmune_contra.append([dd['name'] for dd in demage_relations['no_damage_from']])
        inneficaz_contra.append([dd['name'] for dd in demage_relations['no_damage_to']])

        # Guardar lista traducida en español según lista correspondiente
        super_efectivo_contra_es = en_to_es_list(list(set(flatten(super_efectivo_contra))))
        debil_contra_es =en_to_es_list(list(set(flatten(debil_contra))))
        resistente_contra_es = en_to_es_list(list(set(flatten(resistente_contra))))
        poco_eficaz_contra_es = en_to_es_list(list(set(flatten(poco_eficaz_contra))))
        inmune_contra_es = en_to_es_list(list(set(flatten(inmune_contra))))
        inneficaz_contra_es = en_to_es_list(list(set(flatten(inneficaz_contra))))

        # Completar cuerpo de html
        html_body += f'''<h3>Super efectivo contra:</h3>'''
        html_body += render_pokemon_damage(super_efectivo_contra_es, list(set(flatten(super_efectivo_contra))))
        html_body += f'''<h3>Débil contra:</h3>'''        
        html_body += render_pokemon_damage(debil_contra_es, list(set(flatten(debil_contra))))
        html_body += f'''<h3>Resistente contra:</h3>'''        
        html_body += render_pokemon_damage(resistente_contra_es, list(set(flatten(resistente_contra))))
        html_body += f'''<h3>Poco Eficaz contra:</h3>''' 
        html_body += render_pokemon_damage(poco_eficaz_contra_es, list(set(flatten(poco_eficaz_contra))))
        html_body += f'''<h3>Inmune contra:</h3>''' 
        html_body += render_pokemon_damage(inmune_contra_es, list(set(flatten(inmune_contra))))
        html_body += f'''<h3>Ineficaz contra:</h3>''' 
        html_body += render_pokemon_damage(inneficaz_contra_es, list(set(flatten(inneficaz_contra))))

        # Final de html
        final_html= html_data.html_header + html_body + html_data.html_end
        show_pics(final_html, nombre_pokemon)
        
        break   

    elif opcion ==0:
        print ("""\n \n \n 
        ---------------------------------------------------------------
        Haz decidido salir de la POKEDEX
        Hasta la próxima!         
        \n \n """)
        break

    else:
        print("""\n 
        ---------------------------------------------------------------
                  ¡Comando desconocido! Vuelve a intentarlo por favor""")

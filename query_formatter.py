from constants import PALABRAS_RESERVADAS

query_prueba = "select alumno_id, tipo_documento, primer_apellido, segundo_apellido, primer_nombre, segundo_nombre, fecha_nacimiento, sexo, pais_nac, telefono_alternativo, email, trabaja, sueldo, pension, pensionado, padres_presos, discapacitado, enfermedad, vive_con, embarazada, tiene_hijos, tiene_subsidios, responsable_propio, created_at, updated_at from becasmedias.alumno a"


"""
def check_next_from(lista,elemento):
    try:
        if lista[lista.index(elemento)+1] == "FROM":
            return True
    except:
        None
"""    
def check_next_reservada(lista,elemento):
    try:
        if lista[lista.index(elemento)+1] in PALABRAS_RESERVADAS:
            return True
    except:
        None

def check_not_next_reservada(lista,elemento):
    try:
        if lista[lista.index(elemento)+1] not in PALABRAS_RESERVADAS:
            return True
    except:
        None

def check_not_prev_reservada(lista,elemento):
    try:
        if lista[lista.index(elemento)-1] not in PALABRAS_RESERVADAS:
            return True
    except:
        None

def reservadas_upper(lista):

    for index,elemento in enumerate(lista):
        if palabras_reservadas(elemento):
            lista[index] = elemento.upper()
    
    return lista

def palabras_reservadas(elemento):
    
    return elemento.upper() in PALABRAS_RESERVADAS

def query_formatter(query,debug = False):
    """_summary_

    Args:
        query (_str_): Parametro a ingresar. 
        Ingresar la query con el formato standard del dbeaver luego de apregar CRTL+SPACE

        Ejemplo:
        select * from miescuelamg.becas_media_asentamientos a
        
        CRTL+SPACE

        select id, descripcion, coordenada_x, coordenada_y from miescuelamg.becas_media_asentamientos a 

    Returns:
        _str_: Retorna la query con los nombres de las columnas uno abajo de otro
    """
    ##TODO: GESTIONAR TODAS LAS PALABRAS RESERVADAS DE SQL PARA QUE PUEDAN SER FORMATEADAS. AGREGAR BANDERA PARA LA PALABRA ANTERIOR ASI NO HACE LE SALTO
    ##TODO: POR AHORA FUNCIONA CON UNA QUERY SENCILLA (SELECT * FROM) PROXIMO PASO AGREGAR JOINS,ETC
    ##TODO: TESTEAR QUERY2  
    # SE AGREGO LA TABULACION
    ## TODO: GESTIONAR LA CONDICION DE LAS PALABRAS QUE CONTIENEN UNA COMA  
    
    query_split = query.split()
    query_split = reservadas_upper(query_split)

    if debug:
        print(query_split)

    enter = "\n"
    tab = "\t"
    espacio = " "

    query_formateada = ""

    for elemento in query_split:
        
        if (query_split.index(elemento) == 0): #Para el select
            query_formateada +=elemento+enter
        
        elif (elemento[-1] == ',') or check_next_reservada(query_split,elemento):        
            query_formateada +=tab + elemento+enter     
        else:
            
            if palabras_reservadas(elemento): 
                if check_not_prev_reservada(query_split,elemento) and check_not_next_reservada(query_split,elemento):
                    query_formateada += elemento + espacio
         
                elif check_not_prev_reservada(query_split,elemento) and check_next_reservada(query_split,elemento):
                     query_formateada +=  enter+ elemento + espacio + query_split[query_split.index(elemento)+1] + espacio            
           
            else:
                query_formateada += elemento + espacio

    return query_formateada


if __name__ == "__main__":
    print(f"Query ingresada:\n{query_prueba}")
    print()
    print(f"Query formateada:\n{query_formatter(query_prueba)}") 
    
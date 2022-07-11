import constants

query = "select id, descripcion, coordenada_x, coordenada_y from miescuelamg.becas_media_asentamientos a"

query2 = "select id, solicitud_id, vinculo_responsable_id, primer_apellido_responsable, segundo_apellido_responsable, primer_nombre_responsable, segundo_nombre_responsable, fecha_nacimiento_responsable, sexo_responsable, pais_responsable_id, tipo_documento_responsable_id, documento_responsable, cuil_responsable, telefono_responsable, email_responsable, created_at, updated_at from miescuelamg.becas_media_responsable r left join miescuelamg.becas_media_solicitud s on r.solicitud_id = s.id"

query3 = "select * from aaaaa join ON ASASDASD aaaa"

query4 = "select beneficiario_tipo_registro, beneficiario_id, nombre, apellido, beneficiario_nombre_completo, tipo_documento, numero_documento, correo_electrónico, mail_turnero, telefono_turnero, celular, telefono, telefono_alternativo, nro_serie_equipo, tipo_dispositivo, marca_equipo, estado_equipo, estado_matrícula, grado from miescuelamg.psba_data pd"
query2_split = query2.split()

#query_ingresar = input()

PALABRAS_RESERVADAS = constants.PALABRAS_RESERVADAS

def check_next_from(lista,elemento):
    try:
        if lista[lista.index(elemento)+1] == "FROM":
            return True
    except:
        None
    
def check_next_reservada(lista,elemento):
    try:
        if lista[lista.index(elemento)+1] in PALABRAS_RESERVADAS:
            return True
    except:
        None

def check_not_prev_reservada(lista,elemento):
    try:
        if lista[lista.index(elemento)-1] not in PALABRAS_RESERVADAS:
            return True
    except:
        None

def check_not_next_reservada(lista,elemento):
    try:
        if lista[lista.index(elemento)+1] not in PALABRAS_RESERVADAS:
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

def query_formatter(query):
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
    
    query_split = query.split()
    query_split = reservadas_upper(query_split)

    enter = "\n"
    tab = "\t"
    espacio = " "

    query_formateada = ""

    for elemento in query_split:
        
        if (query_split.index(elemento) == 0):
            query_formateada +=elemento+enter
        
        elif (elemento[-1] == ',') or check_next_from(query_split,elemento):

            query_formateada +=tab + elemento+enter     
        else:
            #
            if palabras_reservadas(elemento): 
                if check_not_prev_reservada(query_split,elemento) and check_not_next_reservada(query_split,elemento):
                    query_formateada += elemento + espacio
                #else:
                #    query_formateada += elemento + espacio + enter
                elif check_not_prev_reservada(query_split,elemento) and check_next_reservada(query_split,elemento):
                     query_formateada +=  enter+ elemento + espacio + query_split[query_split.index(elemento)+1] + espacio            
                #if elemento.upper() == "JOIN" or elemento.upper() == 'ON':
                #    query_formateada +=  elemento + espacio 
                #else:
                #     query_formateada += enter + elemento + espacio  
            else:
                query_formateada += elemento + espacio

    return query_formateada


if __name__ == "__main__":
    print(f"Query ingresada:\n{query2}")
    print()
    print(f"Query formateada:\n{query_formatter(query2)}") 
    #query_split = query.split()
    #print(query_split)
    #print(reservadas_upper(query_split))

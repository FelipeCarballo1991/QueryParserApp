import constants

query = "select id, descripcion, coordenada_x, coordenada_y from miescuelamg.becas_media_asentamientos a"

query2 = "select id, solicitud_id, vinculo_responsable_id, primer_apellido_responsable, segundo_apellido_responsable, primer_nombre_responsable, segundo_nombre_responsable, fecha_nacimiento_responsable, sexo_responsable, pais_responsable_id, tipo_documento_responsable_id, documento_responsable, cuil_responsable, telefono_responsable, email_responsable, created_at, updated_at from miescuelamg.becas_media_responsable r left join miescuelamg.becas_media_solicitud s on r.solicitud_id = s.id"

query2_split = query2.split()

PALABRAS_RESERVADAS = constants.PALABRAS_RESERVADAS


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
    ##TODO: GESTIONAR TODAS LAS PALABRAS RESERVADAS DE SQL PARA QUE PUEDAN SER FORMATEADAS
    ##TODO: POR AHORA FUNCIONA CON UNA QUERY SENCILLA (SELECT * FROM) PROXIMO PASO AGREGAR JOINS,ETC
    ##TODO: TESTEAR QUERY2
    
    query_split = query.split()

    enter = "\n"
    espacio = " "

    query_formateada = ""

    for elemento in query_split:
    
        if (elemento[-1] == ',') or (query_split.index(elemento) == 0):
            query_formateada +=elemento+enter

        else:
            #if elemento == "from" or elemento == "left" or elemento == "inner" or elemento == "join":
            if palabras_reservadas(elemento):
                query_formateada += enter + elemento + espacio   
            else:
                query_formateada += elemento + espacio

    return query_formateada



if __name__ == "__main__":
    print(f"Query ingresada:\n{query2}")
    print()
    print(f"Query formateada:\n{query_formatter(query2)}") 

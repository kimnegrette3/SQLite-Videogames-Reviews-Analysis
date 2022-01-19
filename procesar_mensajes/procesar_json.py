import json
from datetime import date
from cargar_datos import cargar_datos_ddbb as db

    #Escoger solo algunos, porque son muchisimos.
    #La misma idea, si el usuario no está, se inserta, si el videojuego no está, se inserta
    #Se arma la sentencia sql y se inserta el comentario

#Create a method to process the json file and extract the messages
def procesar_mensajes(conexion, file, tit_juego):
    """
    Procesa el archivo json y extrae los mensajes
    :param conn: Conexión a la base de datos SQLite
    :param file: Archivo json
    :param tit_juego: Titulo del juego
    :return:
    """
    with open(file) as json_file:
        json_data = json.load(json_file)
    print(json_data.keys())
    for juego in json_data.keys():
        #print(juego)
        #If the game is in the json file, then process it
        if juego == tit_juego:
            #look for the id_user in the database
            id_juego = db.buscar_juego(conexion, tit_juego)
            #if not found, insert it
            if id_juego is None:
                f_publicacion = json_data[juego]['appInfo']['released']
                id_juego = db.insertar_juego(conexion, tit_juego, "Android", f_publicacion)
            #look for the red_social in the database
            id_red_social = db.buscar_redsocial(conexion, "PlayStoreGame.com")
            #print(juego)
            #Extract a limited nomber of messages and its attributes
            for i in range(5):
                #get the user name
                n_usuario = (json_data[juego]['reviews'][i]['userName'])
                #check if the user is in the database
                id_usuario = db.buscar_usuario(conexion, n_usuario)
                #if not found, insert it
                if id_usuario is None:
                    id_usuario = db.insertar_usuario(conexion, n_usuario)
                #get the message content
                text_mensaje = (json_data[juego]['reviews'][i]['content'])
                #get the message date, which is today
                f_mensaje = date.today()
                #insert the message in the database
                db.insertar_mensaje(conexion, id_usuario, id_juego, id_red_social, f_mensaje, text_mensaje)
            #print the number of messages processed
            print("Se procesaron " + str(i+1) + " mensajes")
        #Else, print an error message
        else:
            print("El juego " + juego + " no está en el archivo")
            




                
    
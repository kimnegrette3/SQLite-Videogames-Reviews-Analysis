import json
from datetime import date
from sqlite3 import Error
from dateutil import parser
from cargar_datos import cargar_datos_ddbb as db

#Create a method to process the json file and extract the messages
def procesar_mensajes(conexion, file, tit_juego):
    """
    Procesa un archivo json, extrae los mensajes y 
    los inserta en la base de datos.
    :param conexion: Conexión a la base de datos SQLite
    :param file: Archivo json con los mensajes
    :param tit_juego: Titulo del juego a procesar
    """
    with open(file) as json_file:
        json_data = json.load(json_file)
    for juego in json_data.keys():
        #if the game is in the json file, then process it
        if juego == tit_juego:
            #look for the id_user in the database
            id_juego = db.buscar_juego(conexion, tit_juego)
            #if not found, insert it
            if id_juego is None:
                fecha = json_data[juego]['appInfo']['released']
                fecha = parser.parse(fecha)
                f_publicacion = fecha.date().year
                id_juego = db.insertar_juego(conexion, tit_juego, "Android", f_publicacion)
            #look for the red_social in the database
            id_red_social = db.buscar_redsocial(conexion, "PlayStoreGame.com")
            #extract messages and its attributes
            for i in range(len(json_data[juego]['reviews'])):
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
                db.insertar_mensaje(conexion, f_mensaje, text_mensaje,  id_juego, id_usuario, id_red_social)                        
            #if db.insertar_mensaje works, print the number of inserted rows in the database
            return f'Se insertaron {i+1} mensajes del juego "{tit_juego}" en la base de datos'
    #if tit_juego is not ins the json.keys(), print a warning message
    if tit_juego not in json_data.keys():
            print("El juego " + tit_juego + " no está en el archivo json")

            




                
    
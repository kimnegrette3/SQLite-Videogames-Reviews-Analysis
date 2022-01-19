#Aqui va a estar el programa para procesar los mensajes de metacritic
#abrir el fichero, procesar la info y guardar en las tablas correspondientes

import pandas as pd
import sqlite3
from sqlite3 import Error
from datetime import date
from cargar_datos import cargar_datos_ddbb as db


#Method to open a csv file and extract data of videogames to append to the database
def cargar_videojuegos(conexion, csv_file):
    """
    Carga los datos de los videojuegos en la base de datos
    :param conexion: Conexión a la base de datos SQLite
    :param csv_file: Archivo csv con los datos de los videojuegos
    :return:"""
    try:
        df_juegos = pd.read_csv(csv_file, header=0, index_col=0,
                                names = ['tit_juego','f_publicacion','Publisher', 'Genre','plataforma','PMetascore', 'Avg','NoPlayers'] )
        df_juegos = df_juegos.loc[:,[ 'tit_juego','plataforma','f_publicacion']]
        df_juegos.to_sql(name="juegos", con=conexion, if_exists='append', index=False)
        return f'{len(df_juegos)} columnas insertadas en la tabla juegos'
    except Error as e:
        print(e)
        return f'Error al insertar los datos en la tabla juegos'


#Create a method to process messages from a csv file and insert them in the database
#leer el csv con los nombres de las columnas y extraer titulo, plataforma, comentario y username con df.loc
#Debe haber un argumento de condicion para que solo se carguen ciertas lineas
#insertar la fecha actual como fecha del mensaje con datetime f_mensaje = f_actual
#Usar la funcion buscar_redsocial para obtener el id de la red social
#Buscar el id del usuario con la funcion buscar_id_usuario
#buscar el id del juego con la funcion buscar_juego
#insertar el mensaje completo en la ddbb con la funcion insertar_mensaje
#La funcion insertar mensaje recibe todas las columnas de la tabla de mensaje y hace un query insert.
#Debe recorrer el df y hacer un query insert por cada fila, y un commit cada vez que se hace un insert


def procesar_mensajes(conexion, csv_file, juego):
    """
    Procesa los mensajes de metacritic
    :param conexion: Conexión a la base de datos SQLite
    :param csv_file: Archivo csv con los mensajes
    :param juego: Titulo del juego
    :return:"""
    try:
        #leer el csv con la condicion dada y extraer titulo, plataforma, comentario y username con df.loc
        df = pd.read_csv(csv_file,  header= 0, index_col = 0,
                        names = ['tit_juego','plataforma','userscore','comentario','username'])
        df_juego = df.loc[(df['tit_juego'] == juego),['tit_juego','plataforma','comentario','username']]
        id_red_social = db.buscar_redsocial(conexion, "MetacriticGame.com")
        #insertar la fecha actual como fecha del mensaje con datetime f_mensaje = fecha actual
        f_mensaje = date.today()
        if len(df_juego) == 0:
            print("Error: No hay datos para procesar, intenta una nueva búsqueda")
        else:
            #Iterar sobre las filas del df 
            for index, row in df_juego.iterrows():
                #Buscar el id del usuario con la funcion buscar_usuario
                id_usuario = db.buscar_usuario(conexion, row['username'])
                #Si no existe el usuario, insertarlo en la ddbb
                if id_usuario == None:
                    id_usuario = db.insertar_usuario(conexion, row['username'])
                #Buscar el id del juego con la funcion buscar_juego
                id_juego = db.buscar_juego(conexion, row['tit_juego'])
                #Si no existe el juego, insertarlo en la ddbb
                if id_juego == None:
                    id_juego = db.insertar_juego(conexion, row['tit_juego'], row['plataforma'], f_mensaje)
                #insertar el mensaje completo en la ddbb con la funcion insertar_mensaje
                db.insertar_mensaje(conexion, f_mensaje,  row['comentario'],  id_juego, id_usuario, id_red_social)
                #retorna el numero de filas insertadas 
            return f'{len(df_juego)} filas insertadas en la tabla mensajes'
    except Error as e:
        print(e)
        return f'Error al insertar los datos en la tabla mensajes'
                
            
            
            
           







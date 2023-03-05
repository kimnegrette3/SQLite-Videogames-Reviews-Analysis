import pandas as pd
from sqlite3 import Error
from datetime import date
from cargar_datos import cargar_datos_ddbb as db


def cargar_videojuegos(conexion, csv_file):
    """
    Carga los datos de los videojuegos en la base de datos
    :param conexion: Conexión a la base de datos SQLite
    :param csv_file: Archivo csv con los datos de los videojuegos
    :return: Filas insertadas en la base de datos"""
    try:
        df_juegos = pd.read_csv(csv_file, index_col=0, header=0,
                                names = ['tit_juego','f_publicacion','Publisher','Genre','plataforma','Metascore', 'Avg_Userscore','No_Players'] )
        df_juegos = df_juegos.loc[:,['tit_juego','plataforma','f_publicacion']]
        df_juegos.to_sql(name="juegos", con=conexion, if_exists='append', index=False)
        return f'{len(df_juegos)} filas insertadas en la tabla juegos'
    except Error as e:
        print('Error al insertar los datos en la tabla juegos')
        print(e)
        return None


def procesar_mensajes(conexion, csv_file, juego):
    """
    Procesa los mensajes de metacritic.com y los inserta en la base de datos
    :param conexion: Conexión a la base de datos SQLite
    :param csv_file: Archivo csv con los mensajes
    :param juego: Titulo del juego a procesar
    :return: Filas insertadas en la base de datos"""
    try:
        #read the csv and extract the relevant columns
        df = pd.read_csv(csv_file,  header= 0, index_col = 0,
                        names = ['tit_juego','plataforma','userscore','comentario','username'])
        df_juego = df.loc[(df['tit_juego'] == juego),['tit_juego','plataforma','comentario','username']]
        id_red_social = db.buscar_redsocial(conexion, "MetacriticGame.com")
        #get the registration date  (today)
        f_mensaje = date.today()
        if len(df_juego) == 0:
            print("Error: No hay datos para procesar, intenta una nueva búsqueda")
        else:
            #iterate over dataframe rows
            for index, row in df_juego.iterrows():
                #look for the user ID
                id_usuario = db.buscar_usuario(conexion, row['username'])
                #if the user ID is not found, insert the user
                if id_usuario is None:
                    id_usuario = db.insertar_usuario(conexion, row['username'])
                #look for the game ID
                id_juego = db.buscar_juego(conexion, row['tit_juego'])
                #if the game ID is not found, insert the game
                if id_juego is None:
                    id_juego = db.insertar_juego(conexion, row['tit_juego'], row['plataforma'], f_mensaje.year)
                #insert the message
                db.insertar_mensaje(conexion, f_mensaje,  row['comentario'],  id_juego, id_usuario, id_red_social)
                #print the number of messages inserted
            return f'Se insertaron {len(df_juego)} mensajes del juego "{juego}" en la base de datos'
    except Error as e:
        print('Error al insertar los datos en la tabla mensajes')
        print(e)
        return None
                
            
            
            
           







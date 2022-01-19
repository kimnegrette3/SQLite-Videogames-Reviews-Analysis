import sqlite3
from sqlite3 import Error

def sql_connection(db_file):
    """ Crea una conexión a una Base de Datos SQLite Local
        :parámetros db_file: base de datos
        :return: el objeto de la conexión a la BBDD o None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
        if conn:
            conn.close()
    return conn

#Method to find a social network in the table red social, check if it exists and return the id
def buscar_redsocial(conexion, nom_redsocial):
    """
    Retorna el id de la red Social
    :param conn: Conexión a la base de datos SQLite
    :param nom_redsocial: Nombre de la red social
    :return: el id de la red social o None si esta no existe
    """
    try:
        cursor = conexion.cursor()
        query = "SELECT id_red_social FROM red_social WHERE nom_red_social = '{}'".format(nom_redsocial)
        cursor.execute(query)
        id = cursor.fetchone()
        if id is None:
            return None
        else:
            return id[0]
    except Error as e:
        print(e)
        return None

#Method to insert a new row in the table red social if it does not exist
def insertar_redsocial(conexion, nom_redsocial, url_redsocial):
    """
    Inserta una nueva red social
    :param conn: Conexión a la base de datos SQLite
    :param nom_redsocial, url_redsocial: nombre y url de la red social
    :return: project id
    """
    id_red_social = buscar_redsocial(conexion, nom_redsocial)
    print("red social", id_red_social)
    if id_red_social is None:
        query = "INSERT INTO RED_SOCIAL (id_red_social, nom_red_social, url_red_social) VALUES (?, ?, ?)"
        datos = (id_red_social, nom_redsocial, url_redsocial)
        insertar = conexion.cursor()
        insertar.execute(query, datos)
        conexion.commit()
        id_red_social = insertar.lastrowid
        print(f'Red social {nom_redsocial} insertada con id {id_red_social}')
        return id_red_social
    else:
        print("La red Social ya existe con el id {}".format(id_red_social))
        return None


#Create a method to find a game in the table juegos, check if it exists and return the id
def buscar_juego(conexion, tit_juego):
    """
    Retorna el id del juego
    :param conn: Conexión a la base de datos SQLite
    :param tit_juego: Nombe del juego
    :return: el id del juego o None si este no existe
    """
    try:
        cursor = conexion.cursor()
        query = "SELECT id_juego FROM juegos WHERE tit_juego = '{}'".format(tit_juego)
        cursor.execute(query)
        id = cursor.fetchone()
        if id is None:
            return None
        else:
            return id[0]
    except Error as e:
        print(e)
        return None

#Create a method to insert a new row in the table juegos if it does not exist
def insertar_juego(conexion, tit_juego, plataforma, f_publicacion):
    """
    Inserta un nuevo juego
    :param conn: Conexión a la base de datos SQLite
    :param tit_juego: Titulo del juego
    :param plataforma: Plataforma del juego
    :param f_publicacion: Fecha de publicación del juego
    :return: project id"""
    id_juego = buscar_juego(conexion, tit_juego)
    if id_juego is None:   
        query = "INSERT INTO JUEGOS (tit_juego, plataforma, f_publicacion) VALUES (?, ?, ?)"
        datos = (tit_juego, plataforma, f_publicacion)
        insertar = conexion.cursor()
        insertar.execute(query, datos)
        conexion.commit()
        id_juego = insertar.lastrowid
        print(f'Juego {tit_juego} insertado con id {id_juego}')
        return id_juego
    else:
        print("El juego ya existe con el id {}".format(id_juego))
        return None


#Create a method to find a user in the table usuario, check if it exists and return the id
def buscar_usuario(conexion, nick_usuario):
    """
    Retorna el id del usuario
    :param conn: Conexión a la base de datos SQLite
    :param nom_usuario: Username
    :return: el id del usuario o None si este no existe
    """
    try:
        cursor = conexion.cursor()
        query = 'SELECT id_usuario FROM usuario WHERE nick_usuario = "{}"'.format(nick_usuario)
        cursor.execute(query)
        id = cursor.fetchone()
        if id is None:
            return None
        else:
            return id[0]
    except Error as e:
        print(e)
        return None

#Create a method to insert a new row in the table usuario if it does not exist
#argument email_usuario is optional
def insertar_usuario(conexion, nick_usuario, nom_usuario="no name", email_usuario="no email"):
    """
    Inserta un nuevo usuario
    :param conn: Conexión a la base de datos SQLite
    :param nick_usuario, nom_usuario, email_usuario: Username, nombre y email del usuario
    :return: project id
    """
    id_usuario = buscar_usuario(conexion, nick_usuario)
    if id_usuario is None:
        query = "INSERT INTO USUARIO (nick_usuario, nom_usuario, email_usuario) VALUES (?, ?, ?)"
        datos = (nick_usuario, nom_usuario, email_usuario)
        insertar = conexion.cursor()
        insertar.execute(query, datos)
        conexion.commit()
        id_usuario = insertar.lastrowid
        #print(f'Usuario {nick_usuario} creado con id {id_usuario}')
        return id_usuario
    else:
        print("El usuario ya existe con el id {}".format(id_usuario))
        return None

#create a method to insert a message in the table mensaje 
#table mensaje has no id_mensaje, it is autoincremental
def insertar_mensaje(conexion, f_mensaje, text_mensaje, id_juego, id_usuario, id_red_social):
    """
    Inserta un nuevo mensaje
    :param conn: Conexión a la base de datos SQLite
    :param f_mensaje, text_mensaje, id_juego, id_usuario, id_red_social: Fecha del mensaje, texto del mensaje, id del juego, id del usuario y id de la red social
    :return: project id
    """
    try:
        query = "INSERT INTO MENSAJE (f_mensaje, text_mensaje, id_juego, id_usuario, id_red_social) VALUES (?, ?, ?, ?, ?)"
        datos = (f_mensaje, text_mensaje, id_juego, id_usuario, id_red_social)
        insertar = conexion.cursor()
        insertar.execute(query, datos)
        conexion.commit()
        return insertar.lastrowid
    except Error as e:
        print(e)
        return None


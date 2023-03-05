import requests
from datetime import date
from bs4 import BeautifulSoup
from sqlite3 import Error
from urllib.error import HTTPError, URLError
from dateutil import parser
from cargar_datos import cargar_datos_ddbb as db


def procesar_mensajes_game(conexion, url):
    """
    Extrae los mensajes de una página web y los inserta en la base de datos
    :param conexion: Conexión a la base de datos SQLite
    :param url: Url de la página web
    :return: Numero de mensajes insertados en la base de datos"""
    try:
        #create a request to the url
        r = requests.get(url)   
    except HTTPError as e:
        print(e)
    except URLError as e:
        print(e)
    else:
        #create a beautiful soup object
        soup = BeautifulSoup(r.text, 'html.parser')
        #get the title of the game
        tj = soup.select("h1 > span")
        tit_juego = tj[0].get_text("class").strip() #[0] because is the only one
        #get the id of the game
        id_juego = db.buscar_juego(conexion, tit_juego)
        #if not found, insert it
        if id_juego is None:
            plat = soup.select("dl > dd > a[class$='active'] > span") #the one "active" in bold 
            plataforma = plat[0].get_text("class").strip() #[0] is the platform, [1] is the edition
            f_publicacion = date.today().year
            id_juego = db.insertar_juego(conexion, tit_juego, plataforma, f_publicacion)
        #get the list of users
        users = soup.select("article[class='comments-media'] > h4 > span[class='cm-txt u-caps']")
        usuarios = [u.text.split(' ')[0].strip() for u in users]
        #get the dates
        dates = soup.select("article[class='comments-media'] > h4 > span[class='cm-txt text-muted']")
        fechas_m = [d.text.split(' ')[2].strip() for d in dates] #[2] is the date without time.
        #convert to date format
        f_mensajes = [str((parser.parse(f)).date()) for f in fechas_m] 
        #get the messages
        comments = soup.select("article[class='comments-media'] > p")
        text_mensajes = [c.get_text("class").strip() for c in comments]
        #define the social network
        red_social = "GAME"
        id_red_social = db.buscar_redsocial(conexion, red_social)
        #link the users, dates and messages and insert them in the database
        for i in range(len(usuarios)):
            id_usuario = db.buscar_usuario(conexion, usuarios[i])
            if id_usuario is None:
                id_usuario = db.insertar_usuario(conexion, usuarios[i])
            db.insertar_mensaje(conexion, f_mensajes[i], text_mensajes[i], id_juego, id_usuario, id_red_social)
        #print the number of messages inserted in the database
        return f"Se han insertado {len(usuarios)} mensajes del juego {tit_juego} en la base de datos"
 







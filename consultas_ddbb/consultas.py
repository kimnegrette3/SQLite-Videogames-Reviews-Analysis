
Profesor  21 a Todos

SELECT nick_usuario FROM usuario
WHERE id_usuario in (SELECT id_usuario FROM mensaje WHERE text_mensaje like "%game" AND (f_mensaje >= DATE("2022-01-15") AND f_mensaje <= DATE("2022-01-18")))


Profesor  21 a Todos

SELECT nick_usuario, count(text_mensaje) as cantidad
FROM mensaje
INNER JOIN usuario ON usuario.id_usuario = mensaje.id_usuario
GROUP BY mensaje.id_usuario HAVING text_mensaje like "%game" ORDER BY cantidad DESCSELECT nick_usuario, count(text_mensaje) as cantidad
FROM mensaje
INNER JOIN usuario ON usuario.id_usuario = mensaje.id_usuario
GROUP BY mensaje.id_usuario HAVING text_mensaje like "%game" ORDER BY cantidad DESC


Profesor  21 a Todos

SELECT nick_usuario, count(text_mensaje) as cantidad
FROM mensaje
INNER JOIN usuario ON usuario.id_usuario = mensaje.id_usuario
GROUP BY mensaje.id_usuario ORDER BY cantidad DESC


Profesor  21 a Todos

SELECT tit_juego, count(mensaje.id_juego) as cantidad
FROM mensaje INNER JOIN juegos ON mensaje.id_juego = juegos.id_juego
GROUP BY mensaje.id_juego ORDER BY cantidad DESC



Profesor  21 a Todos

SELECT nom_red_social, count(mensaje.id_juego) as cantidad
FROM mensaje INNER JOIN red_social ON mensaje.id_red_social = red_social.id_red_social
GROUP BY mensaje.id_red_social ORDER BY cantidad DESC




def consultar_comentarios_fecha(conexion, palabra, fecha1, fecha2): # , palabra, fecha1, fecha2
    """
    Dado un rango entre dos fechas y un texto, obtener aquellos usuarios que incluyen en sus mensajes una 'palabra'
    en medio de una frase
    """
    query = 'SELECT nick_usuario FROM usuario WHERE id_usuario in (SELECT id_usuario FROM mensaje WHERE text_mensaje like "%{}" AND f_mensaje >= (DATE({}) AND f_mensaje <= DATE({})))'.format(palabra, fecha1, fecha2)
    df = pd.read_sql_query(query, conexion)
    #print(df) comentar si se hace desde jupyter
    return df


def consultas_comentarios_palabra





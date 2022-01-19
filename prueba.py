from cargar_datos import cargar_datos_ddbb as db
from procesar_mensajes import procesar_csv as csv
from procesar_mensajes import procesar_json as js


#inserta los mensajes del juego SuperMario en la tabla mensajes
con = db.sql_connection('ddbb/videojuegos.db')
#file = 'data/metacritic_game_user_comments.csv'
#csv.procesar_mensajes(con, file, "God of War III Remastered")
#csv.procesar_mensajes(con, file, "Super Mario Galaxy")
#csv.procesar_mensajes(con, file, "Final Fantasy IX")
#csv.procesar_mensajes(con, file, "Mario Kart Super Circuit")
#csv.procesar_mensajes(con, file, "The Witcher 3: Wild Hunt")
#csv.procesar_mensajes(con, file, "Star Wars: Knights of the Old Republic")

#a = db.buscar_juego(con, "Super Mario Galaxy")
#print(a)

#db.insertar_redsocial(con, 'Twitter', 'www.twitter.com')

#b = db.buscar_redsocial(con, "Twitter")
#print(b)

#c = db.buscar_usuario(con, "Dante'sLame")
#print(c)

#db.insertar_usuario(con, "Dante'sLame")
file = 'PlayStoreGameAppInfoReview.json'
js.procesar_mensajes(con, )
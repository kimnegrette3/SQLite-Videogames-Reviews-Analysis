#Este será el programa principal desde el que se va a ejecutar todo.
#Se recomienda primero hacer las funciones con datos ficticios
#importar todos los módulos
from cargar_datos import cargar_datos_ddbb as ddbb
from procesar_mensajes import procesar_mensaje_metacritic as meta

conexion = ddbb.sql_connection('ddbb/videojuegos.db')
#ddbb.buscar_redsocial(conexion, "Amazon.com")
#ddbb.insertar_redsocial_bbdd(conexion, "Facebook", "www.facebook.com")
#meta.cargar_videojuegos()
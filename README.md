# Videogames Reviews Analysis

## Descripción
El proyecto final tiene como objetivo principal la creación de una aplicación que permita gestionar los mensajes obtenidos de diversos videojuegos en diferentes redes sociales. Esta aplicación se desarrolla a solicitud de nuestra empresa de videojuegos y se utiliza para consolidar y analizar comentarios y feedback de jugadores.

## Características Principales
### Ingesta de Datos: 
La aplicación puede importar comentarios desde diversas fuentes:
Play Store Game a través del archivo PlayStoreGameAppInfoReview.json.
Metacritic Game usando el archivo metacritic_game_user_comments.csv.
Extracción de comentarios directamente desde páginas web.
### Almacenamiento Unificado: 
Todos los comentarios y mensajes son almacenados en una base de datos relacional, manteniendo una estructura uniforme independientemente de su origen.
### Interfaz de Usuario: 
Se proporciona una interfaz de usuario sencilla, accesible a través de Jupyter Notebook o ejecutando directamente el script main.py, que permite:
Carga inicial de datos de juegos y plataformas.
Adición de mensajes a la base de datos, vinculando cada mensaje con un videojuego específico.
Realización de consultas específicas sobre los mensajes almacenados.
## Uso
### Carga Inicial: 
Inicia la aplicación y utiliza la opción para cargar datos iniciales desde metacritic_game_info.csv.
### Importar Mensajes: 
Selecciona la fuente desde la cual deseas importar los comentarios. Si estás importando desde un archivo, asegúrate de tener el archivo correspondiente en el directorio adecuado.
### Consultas:
Rango de Fechas y Texto: Proporciona dos fechas y un texto para obtener una lista de usuarios que mencionan el texto en sus comentarios durante ese periodo.
Mensajes por Usuario: Muestra la cantidad de mensajes que cada usuario ha publicado.
Media de Mensajes Diarios: Indica un rango de fechas y obtén un histograma que muestra la media de mensajes diarios por red social.
Estadísticas por Tema: Define un tema a través de un conjunto de palabras clave y descubre en qué red social se habla más sobre ese tema.
Interfaz: Puedes interactuar con la aplicación a través de una notebook ejecutable de Jupyter o ejecutando main.py desde tu terminal.

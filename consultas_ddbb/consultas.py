import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd
from dateutil import parser


def consultar_comentarios_fecha(conexion, palabra, fecha1, fecha2):
    """
    Dado un rango entre dos fechas y un texto, obtiene aquellos usuarios
    que incluyen en sus mensajes una 'palabra' específica.
    :param conexion: Conexión a la base de datos SQLite
    :param fecha1, fecha2: Fecha inicial y final
    :param palabra: Palabra a buscar en los comentarios
    """
    f1 = parser.parse(fecha1).date()
    f2 = parser.parse(fecha2).date()
    query = f'''SELECT nick_usuario, count(text_mensaje) as cantidad FROM mensaje
                INNER JOIN usuario ON usuario.id_usuario = mensaje.id_usuario
                GROUP BY mensaje.id_usuario HAVING text_mensaje like "%{palabra}%" AND (f_mensaje >= DATE("{f1}") AND f_mensaje <= DATE("{f2}")) 
                ORDER BY cantidad DESC'''
    df = pd.read_sql_query(query, conexion)
    #print only the nick_usuario and the count of messages
    print(f'Los usuarios que han escrito un mensaje con la palabra "{palabra}" entre las fechas {fecha1} y {fecha2} son:')
    return df.style


def consultar_comentarios_usuario(conexion):
    """ 
    Obtiene la cantidad de mensajes por usuario en la base de datos
    :param conexion: Conexión a la base de datos SQLite
    """
    query = '''SELECT nick_usuario, count(text_mensaje) as cantidad 
                FROM mensaje INNER JOIN usuario ON usuario.id_usuario = mensaje.id_usuario 
                GROUP BY mensaje.id_usuario 
                ORDER BY cantidad DESC'''
    df = pd.read_sql_query(query, conexion)
    print('La cantidad de mensajes por usuario son:')
    return df.style


def consultar_comentarios_red_social_fecha(conexion, fecha1, fecha2):
    """
    Dado un rango entre dos fechas, obtiene la cantidad media de mensajes 
    por red social en ese periodo en la base de datos
    :param conexion: Conexión a la base de datos SQLite
    :param fecha1, fecha2: Fecha inicial y final
    """
    f1 = parser.parse(fecha1).date()
    f2 = parser.parse(fecha2).date()
    query = f'''SELECT nom_red_social, count(mensaje.id_usuario) as total
                FROM mensaje INNER JOIN red_social ON mensaje.id_red_social = red_social.id_red_social
                WHERE f_mensaje >= DATE("{f1}") AND f_mensaje <= DATE("{f2}")
                GROUP BY nom_red_social ORDER BY total DESC'''    
    df = pd.read_sql_query(query, conexion)
    days = (f2 - f1).days
    #calculate the average daily number of messages per social network
    df['media_diaria'] = df['total'] / days
    sb.set_style("whitegrid")
    b = sb.barplot(x='nom_red_social', y='media_diaria', data=df)
    b.set_title('Media diaria de mensajes por red social')
    b.set_xlabel('Red social')
    b.set_ylabel('Media diaria de mensajes')
    plt.show(b)
    print(f'La red social con más mensajes durante este periodo fue {df["nom_red_social"].iloc[0]} con un promedio de {round(df["media_diaria"].iloc[0], 2)} mensajes por día')


def consultar_tema_red_social(conexion, palabra1, palabra2, palabra3):
    """
    Dado un texto, obtiene la red social que más mensajes incluye con ese tema
    :param conexion: Conexión a la base de datos SQLite
    :param palabra1, palabra2, palabra3: Palabras a buscar en los comentarios
    """
    #extract the message text and the social network
    query = f'''SELECT nom_red_social, text_mensaje
                FROM mensaje
                INNER JOIN red_social ON mensaje.id_red_social = red_social.id_red_social
                GROUP BY mensaje.id_usuario
                ORDER BY nom_red_social'''
    df = pd.read_sql_query(query, conexion)
    pat = r"{}|{}|{}".format(palabra1, palabra2, palabra3)
    #count the number of times the topic appears in the message text
    df['conteo'] = df.text_mensaje.str.count(pat)
    #group by social network
    d = df.groupby('nom_red_social')
    #get the descriptive statistics
    des = d.describe()
    #add the sum of topic appearances to the dataframe
    des.loc[:, ('conteo', 'sum')] = d.sum()['conteo']
    #print the statistics
    print(des['conteo'].to_string(columns = ['count', 'sum', 'mean', 'min', 'max']),'\n')
    #plot the results
    sb.set_style("whitegrid")
    a = sb.boxplot(x = 'nom_red_social', y = 'conteo', data = df)
    a.set_title('Cantidad de mensajes por red social')
    a.set_xlabel('Red social')
    a.set_ylabel('Número de mensajes')
    plt.show(a)
    #print the social network with the highest number of messages including the topic
    print(f"La red social donde más se habla de este tema es {des['conteo']['mean'].idxmax()}\n")
  




    
   

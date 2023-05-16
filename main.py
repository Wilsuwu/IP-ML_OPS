from fastapi import FastAPI
import pandas as pd
import calendar
from datetime import datetime
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity



app = FastAPI()

@app.get("/")
def read_root():
    return{"Hello":"World"}

@app.get('/peliculas_mes/{mes}')
def peliculas_mes(mes: str) -> dict:
    # Diccionario para hacer la traducción de nombres de mes de español a inglés
    meses_dict = {"enero":"January", "febrero":"February", "marzo":"March", "abril":"April", "mayo":"May", "junio":"June",
                  "julio":"July", "agosto":"August", "septiembre":"September", "octubre":"October", "noviembre":"November",
                  "diciembre":"December"}

    # Cargamos el archivo CSV
    peliculas = pd.read_csv('df_funciones.csv')

    # Convierte la columna "release_date" a formato de fecha
    peliculas["release_date"] = pd.to_datetime(peliculas["release_date"], errors="coerce")

    # Traduce el nombre de mes ingresado a su equivalente en inglés
    mes_en = meses_dict.get(mes.lower(), None)
    if mes_en is None:
        return {"error": "El mes ingresado no es válido"}

    # Filtra las películas que se estrenaron en el mes especificado
    peliculas_filtradas = peliculas[peliculas["release_date"].dt.month == pd.to_datetime(mes_en, format="%B").month]

    # Cuenta la cantidad de películas filtradas
    cantidad_peliculas = len(peliculas_filtradas)

    # Traduce el nombre del mes en inglés de vuelta a español
    mes_es = [key for key, value in meses_dict.items() if value == mes_en][0]

    return {"mes": mes_es.capitalize(), "cantidad": cantidad_peliculas}



@app.get('/peliculas_dia/{dia}')
def peliculas_dia(dia: str) -> dict:
    # Leer el dataset de películas
    peliculas = pd.read_csv('df_funciones.csv')

    
    dia_num = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo'].index(dia)

    
    # convertimos la columna 'release_date' a datetime (just in case)
    peliculas['release_date'] = pd.to_datetime(peliculas['release_date'], format='%Y-%m-%d')


    # Filtrar películas que se estrenaron en el día de la semana dado
    peliculas_en_dia = peliculas[peliculas['release_date'].dt.weekday == dia_num]

    


    # Filtrar películas que tengan una fecha de estreno válida
    peliculas_con_fecha_valida = peliculas_en_dia[peliculas_en_dia['release_date'].notnull()]

    cantidad = peliculas_con_fecha_valida.shape[0]

    # Retornar un diccionario con el día y la cantidad de películas
    return {'dia': dia, 'cantidad': cantidad}



@app.get('/franquicia/{franquicia}')
def franquicia(franquicia):
    # Leer el dataset de películas
    peliculas = pd.read_csv('df_funciones.csv')
    
    # Filtrar las películas por la franquicia especificada
    peliculas_franquicia = peliculas[peliculas['belongs_to_collection'] == franquicia]
    
    # Obtener la cantidad de películas en la franquicia
    cantidad = len(peliculas_franquicia)
    
    if cantidad > 0:
        # Calcular la ganancia total de la franquicia
        ganancia = peliculas_franquicia['revenue'].sum()
        
        # Calcular la ganancia promedio de la franquicia
        ganancia_promedio = ganancia / cantidad
        
        # Devolver un diccionario con los resultados
        return {'franquicia': franquicia, 'cantidad': cantidad, 
                'ganancia_total': ganancia, 'ganancia_promedio': ganancia_promedio}
    else:
        # Si no hay películas en la franquicia, devolver un mensaje de error
        return {'franquicia': franquicia, 'error': 'No se encontraron películas en esta franquicia.'}
    

@app.get('/peliculas_pais/{pais}')
def peliculas_pais(pais):

    #Leemos el dataset con la informacion
    peliculas = pd.read_csv('df_funciones.csv')

    
    # Separamos la columna que necesitamos para este caso
    paises = peliculas['production_countries']
    
    
    # Creamos un contador para guardar la cantidad
    cantidad = 0

    #Aplicamos un ciclo for para recorrer la variable paises
    for pelicula in paises:

        if pelicula == pais:
        
            cantidad += 1

            
    return {'pais': pais, 'cantidad': cantidad}
    

@app.get('/productoras/{productora}')
def productoras(productora: str):
    # Leer los datos de un archivo csv con la información de las películas
    # producidas por cada productora
    data = pd.read_csv('df_funciones.csv')

    # Filtrar las filas que corresponden a la productora ingresada
    data_productora = data[data['production_companies'] == productora]

    # Calcular la ganancia total y la cantidad de películas producidas
    ganancia_total = data_productora['revenue'].sum()
    cantidad_peliculas = len(data_productora)

    # Retornar un diccionario con la información
    return {'productora': productora, 'ganancia_total': ganancia_total, 'cantidad': cantidad_peliculas}


@app.get('/retorno/{pelicula}')
def retorno(pelicula:str):
    '''Ingresas la pelicula, retornando la inversion, la ganancia, el retorno y el año en el que se lanzo'''
    
    data = pd.read_csv('df_funciones.csv')
    data['release_date'] = pd.to_datetime(data['release_date'], format='%Y-%m-%d')

    
    pelicula_df = data.loc[data['title'] == pelicula]
    inversion = pelicula_df['budget'].values[0]
    ganancia = pelicula_df['revenue'].values[0]
    retorno = pelicula_df['return'].values[0]
    anio = pelicula_df['release_date'].dt.year.values[0]
    año = int(anio)

    
    return {'pelicula':pelicula, 'inversion':inversion, 'ganacia':ganancia,'retorno':retorno, 'anio':año}




# Sistema de recomendacion de peliculas

df = pd.read_csv('movies_ML_sample10.csv')

# Cremos un objeto de la clase tfidvectorizer y eliminamos las stopwords que no aportan valor al analisis
tfidf = TfidfVectorizer(stop_words='english')

#De quedar valores NaN, nos aseguramos de que no:
df['processed_overview'] = df['processed_overview'].fillna('')

#Transformamos la columna en una matriz de caracteristicas TF-IDF
tfidf_matrix = tfidf.fit_transform(df['processed_overview'])


cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

indices = pd.Series(df.index, index=df['title']).drop_duplicates()


@app.get('recomendacion/{titulo}')
def recomendacion(titulo:str):
    idx = indices[titulo]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]
    movie_indices = [i[0] for i in sim_scores]
    respuesta = list(df[['title']].iloc[movie_indices])
    return {'Lista recomendada': respuesta}
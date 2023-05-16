Sistema de Recomendacion de Peliculas

VIDEO:



ETL Y DATASETS:

En este repositorio encontraran un procesamiento de ETL del archivo movies_dataset.csv:(https://drive.google.com/file/d/1Rp7SNuoRnmdoQMa5LWXuK4i7W1ILblYb/view),
el mismo fue transformado en distintos sets de datos como 'movies_df', 'df_funciones.csv' y 'moves_ML_sample10.csv'. Los cuales tienen las siguientes finalidades:

'movies_df.csv': Es el archivo procesado y producto del ETL el cual contiene las transformaciones sugeridas y unas extra a mi criterio detalladas en el archivo 'Limpieza_movies'

'df_funciones.csv': Es un archivo optimizado para las funciones creadas en el archivo 'main.py' que se encuentran ahora mismo subidas a la api, la cual pueden consultar cuando gusten
desde la API con el siguiente enlace: https://proyectofastapi.onrender.com/docs#/default



'movies_ML_sample10.csv': Es el archivo usado para el modelo de ML, el cual contiene solo el 10% del archivo procesado ('movies_df') por cuestiones de hardware

Continuando con el proyecto tenemos el EDA, en el cual concluí segun mi analisis cuales eran las variables relevantes y a tener en cuenta para mi modelo de ML
de Recomendacion de Peliculas. 
Las mismas se encuentran comentadas en el mismo archivo paso a paso. El producto final de este es una funcion que se le ingresa un titulo de una pelicula y este
devolvera un top 5 de peliculas recomendadas en base a la ingresada.

En el archivo 'requirementes.txt' se encuentran todos los softwares necesarios para correr el proyecto en cualquier ordenador.



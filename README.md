  Primer Proyecto Individual

Bienvenidos a mi primer proyecto individual
En este me desempeñaré como un MLOps Engineer

Este proyecto se subdivide en dos partes: una de Data Engineer (Ingenieria de Datos) donde hacemos el ETL (Extraccion-Transformacion-Carga) de los datos, se desarrola desde cero una API con la ayuda del framework FastAPI y finalizamos haciendo el Deploy de nuestra API por medio Render que es una nube unificada para crear y ejecutar aplicaciones y sitios web, entre otros. En el archivo ETL_endpoints.ipynb encontraras el desarrollo de esta parte junto con la creacion de funciones a ser usadas en los endpoints de FastAPI.

Por otro lado tenemos la parte de Machine Learning (ML) donde crearemos un sistema de recomendacion de peliculas donde haremos un EDA (Analisis Exploratorio de Datos), donde, una vez finalizado decidiremos que datos son relevantes para ser usados por nuestro modelo de recomendacion. En los archivos EDA.ipynb y Modelo.ipynb encontraras el desarrollo de esta parte


El proceso de ETL es un proceso de Extraccion, Transformacion y Carga en el cual cargamos datos desde un archivo principal  (https://drive.google.com/file/d/1Rp7SNuoRnmdoQMa5LWXuK4i7W1ILblYb/view), los transformamos segun las necesidades del proyecto y analisis individuales. Y finalmente lo exportamos como un archivo nuevo listo para la siguiente etapa.

En las siguientes lineas describo cada uno de los archivos del repositorio:

  ETL Y DATASETS:

En este repositorio encontraran un procesamiento de ETL del archivo movies_dataset.csv:,
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


  EDA y ML
  
En esta etapa hacemos un analisis más especifico para el desarrollo de nuestro modelo de ML.
El cual es un modelo de aprendizaje no supervisado el cual tiene la finalidad de recomendarte 5 peliculas similares a la ingresada.

Puedes consultar que peliculas estan listadas en el archivo 'movies_ML_sample10' el cual contiene solo el 10% del dataset original luego de todos los procesos anteriores, este tuvo que ser reducido a modo de optimizacion.

A continuacion te dejo una lista de Peliculas que puedes ingresar como ejemplo:

- The Time Being
- Bloody Murder
- About Alex
- California
- Marie Curie

Entre otras.

  API

Finalmente el proyecto fue deployado sobre render, tenemos nuestra API desarrollada con FastAPI funcionando correctamente.
En el siguiente video te explico como puedes hacer consultas sobre la misma: https://youtu.be/u32b-v3tP7Q


INSTALACION

Si deseas instalar todo en tu ordenador y probarlo desde allí te recomiendo primero crear un entorno virtual.
Una vez dentro del mismo utilizar el comando pip install -r requirements.txt para instalar las librerias con sus versiones necesarias.
Este comando instalara automaticamente todas las librerias contenidas en el archivo requirements.txt.



Agradecimientos:

Agradecer a todo el equipo de HENRY encargado de la seccion de LABS por su colaboracion y compromiso con esta tarea. 
De igual manera quiero agradecer a todos los compañeros de la cohorte FT10 por siempre ayudar voluntariamente cuando uno lo necesita.




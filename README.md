# TheHungerGamesData

Autores:
- Pablo Fernández González
- Sara Guillén Torrado

## Herramientas

- Python
  - Pandas
  - Flask
  - Neo4j
  - Matplotlib
- Neo4j
- VSC
- Anaconda
- Jupyter Notebook
- GitHub

## Dataset

`HungerGames_Character_Dataset_ALL.csv` es un dataset realizado desde cero por los autores del proyecto. Contiene información sobre los personajes de la saga de libros "Los Juegos del Hambre" de Suzanne Collins. El dataset incluye las siguientes columnas.

## Conexión a la base de datos

Para que la aplicación funcione, el servidor de Neo4j debe estar en ejecución. La conexión se establece desde el `main.ipynb`, a través de variables de tipo String. Se deben modificar para adaptarlas a la configuración específica del usuario.

## Carga de datos

La última celda de `main.ipynb` contiene el código para cargar el dataset en la base de datos. Se debe ejecutar después de establecer la conexión con la base de datos. El código utiliza la librería `pandas` para leer el archivo CSV y luego utiliza la API de Neo4j para cargar los datos en la base de datos.  

Antes de cargar los datos, se eliminan todos los nodos y relaciones previamente creados para evitar redundancias.

## Ejecución de la aplicación

Para ejecutar la aplicación, se debe abrir el archivo `main.ipynb`. Asegúrate de que todas las celdas se ejecuten en orden. La aplicación utiliza Flask para crear una API RESTful que permite realizar consultas a la base de datos de Neo4j. La aplicación está diseñada para ser ejecutada en un entorno local y no está destinada a producción.
import pandas as pd
import pandas.io.sql as PBD

def importar_CSV(ruta):
    print("--------------------------------------------")

    try:
        df=pd.read_csv(ruta, delimiter=",", encoding="ISO-8859-1")
        print("Se ha importado el archivo CSV correctamente")

        return(df)

    except PBD.DatabaseError as error:
        print("Error. No se ha podido importar de CSV")
        print(error)

    print("--------------------------------------------")


def exportar_CSV(ruta,df):
    print("--------------------------------------------")

    try:
        df.to_csv(ruta, sep=";", index=False) #index a False para no escribir la columna índice
        print("Se ha exportado el archivo CSV correctamente")

    except PBD.DatabaseError as error:
        print("Error. No se ha podido exportar a CSV")
        print(error)

    print("--------------------------------------------")

def consultar_atributos(df):
    try:
        print("-------------------------")
        print("---consultar_atributos---")
        print("-------------------------")

        print("---head - Primeros valores (5 por defecto, 3 en este caso)---") # Por defecto muestra 5 elementos
        print(df.head(3)) # Mostrar los 3 primeros elementos

        print("---tail - Últimos valores (5 por defecto)---") # Por defecto muestra 5 elementos
        print(df.tail())

        print("---info - Información sobre el archivo CSV (columnas, uso de memoria, tipos...)---")
        print(df.info())

        print("---shape - Número de filas y columnas, respectivamente---")
        print(df.shape)

        print("---size - Número total de casillas (filas por columnas)---")
        print(df.size)

        print("---columns - Columnas---")
        print(df.columns)

        print("---index - Índice de la tabla---")
        print(df.index)

        print("---dtypes - Tipos de datos---")
        print(df.dtypes)

        print("--------------------------------")
        print("---Fin de consultar_atributos---")
        print("--------------------------------")

    except PBD.DatabaseError as error:
        print("Error. Problema en atributos de dataFrame")
        print(error)

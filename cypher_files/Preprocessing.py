import pandas as pd
import pandas.io.sql as PBD

ruta_csv='C:\\Users\\PC\\HungerGames_Characters_Dataset_ALL.csv'

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

def create_neo4j_district_nodes(values, filename="cypher_files/create_districts.cypher"):
    with open(filename, "w", encoding="utf-8") as file:
        for val in values:
            if val != 0:
                file.write(f"CREATE (:District {{Name: 'District {val}', Number: {val}}});\n")
            elif val == 0:
                file.write(f"CREATE (:District {{Name: 'The Capitol', Number: {val}}});\n")
            else:
                file.write(f"CREATE (:District {{Name: '???', Number: -1}});\n")

def create_neo4j_game_year_nodes(games, filename="cypher_files/create_game_years.cypher"):
    all_years = set()
    for val in games:
        if pd.isna(val):
            continue
        parts = [a.strip() for a in str(val).split(",")]
        all_years.update(parts)

    with open(filename, "w", encoding="utf-8") as file:
        for year in sorted(all_years):
            file.write(f"CREATE (:Game_Year {{Year: {year}, Description: 'None'}});\n")

def create_neo4j_book_nodes(books, filename="cypher_files/create_books.cypher"):
    all_books = set()
    for val in books:
        if pd.isna(val):
            continue
        parts = [a.strip() for a in str(val).split(",")]
        all_books.update(parts)

    with open(filename, "w", encoding="utf-8") as file:
        for book in sorted(all_books):
            safe_name = book.replace("'", "`")
            order = -1

            match safe_name:
                case "The Hunger Games":
                    order = 1
                case "Catching Fire":
                    order = 2
                case "Mockingjay":
                    order = 3
                case "The Ballad of Songbirds and Snakes":
                    order = 4
                case "Sunrise on the Reaping":
                    order = 5
                case "Mentioned":
                    order = 6

            if safe_name not in ["Trilogy"]:
                file.write(f"CREATE (:Book {{Title: '{safe_name}', Order: '{order}', Description: 'None'}});\n")

def create_neo4j_alliance_nodes(alliances, filename="cypher_files/create_alliances.cypher"):
    all_alliances = set()
    for val in alliances:
        if pd.isna(val):
            continue
        parts = [a.strip() for a in str(val).split(",")]
        all_alliances.update(parts)

    with open(filename, "w", encoding="utf-8") as file:
        for alliance in sorted(all_alliances):
            safe_name = alliance.replace("'", "`")
            if safe_name not in ["Katniss", "Haymitch"]:
                file.write(f"CREATE (:Alliance {{Name: '{safe_name}', Description: 'None'}});\n")

def create_neo4j_character_nodes(df, filename="cypher_files/create_characters.cypher"):
    allowed_columns = ["ID", "Name", "Gender", "Profession"]
    with open(filename, "w", encoding="utf-8") as file:
        for _, row in df.iterrows():
            props_list = []
            for col in allowed_columns:
                if col in df.columns:
                    value = row[col]
                    if pd.isna(value) and col == "Profession":
                        value = "None"
                    if not pd.isna(value):
                        safe_value = str(value).replace("'", "`")
                        props_list.append(f"{col}: '{safe_value}'")
            props = ", ".join(props_list)
            file.write(f"CREATE (:Character {{{props}}});\n")

# -------------------------------------------------------------------------------------

def create_character_district_links(df, filename="cypher_files/link_characters_districts.cypher"):
    with open(filename, "w", encoding="utf-8") as file:
        for _, row in df.iterrows():
            character_id = str(row["ID"])
            district = row["District"]

            if pd.isna(character_id) or pd.isna(district):
                continue

            file.write(
                f"MATCH (c:Character {{ID: {character_id}}}), (d:District {{Number: {int(district)}}})\n"
                f"CREATE (c)-[:FROM_DISTRICT]->(d);\n"
            )

def create_character_game_links(df, filename="cypher_files/link_characters_games.cypher"):
    with open(filename, "w", encoding="utf-8") as file:
        for _, row in df.iterrows():
            character_id = str(row["ID"])
            games = row.get("Game_Year", None)
            winner = str(row.get("Winner", "No")).strip().lower()

            if pd.isna(character_id) or pd.isna(games):
                continue

            winner_flag = "true" if winner == "yes" else "false"

            years = [g.strip() for g in str(games).split(",")]

            for year in years:
                if year.isdigit():
                    year_int = int(year)
                    if year_int == 75:
                        file.write(
                            f"MATCH (c:Character {{ID: {character_id}}}), (g:Game_Year {{Year: {year_int}}})\n"
                            f"CREATE (c)-[:PARTICIPATED_IN {{victor: false}}]->(g);\n"
                        )
                    else:
                        file.write(
                            f"MATCH (c:Character {{ID: {character_id}}}), (g:Game_Year {{Year: {year_int}}})\n"
                            f"CREATE (c)-[:PARTICIPATED_IN {{victor: {winner_flag}}}]->(g);\n"
                        )

def create_character_book_links(df, filename="cypher_files/link_characters_books.cypher"):
    trilogy_books = ["The Hunger Games", "Catching Fire", "Mockingjay"]

    with open(filename, "w", encoding="utf-8") as file:
        for _, row in df.iterrows():
            character_id = str(row["ID"])
            books = row.get("Appearance", None)

            if pd.isna(character_id) or pd.isna(books):
                continue

            book_list = [b.strip() for b in str(books).split(",")]

            for book in book_list:
                if book == "Trilogy":
                    expanded_books = trilogy_books
                elif book != "None":
                    expanded_books = [book]
                else:
                    continue

                for title in expanded_books:
                    safe_book = title.replace("'", "`")
                    file.write(
                        f"MATCH (c:Character {{ID: {character_id}}}), (b:Book {{Title: '{safe_book}'}})\n"
                        f"CREATE (c)-[:APPEARS_IN]->(b);\n"
                    )

def create_character_alliance_links(df, filename="cypher_files/link_characters_alliances.cypher"):
    with open(filename, "w", encoding="utf-8") as file:
        for _, row in df.iterrows():
            character_id = str(row["ID"])
            alliances = row.get("Alliance", None)

            if pd.isna(character_id) or pd.isna(alliances):
                continue

            alliance_list = [a.strip() for a in str(alliances).split(",")]

            for alliance in alliance_list:
                if alliance == "Katniss":
                    file.write(
                        f"MATCH (c:Character {{ID: {character_id}}}), (k:Character {{Name: 'Katniss Everdeen'}})\n"
                        f"CREATE (c)-[:ALLY_OF]->(k);\n"
                    )
                elif alliance == "Haymitch":
                    file.write(
                        f"MATCH (c:Character {{ID: {character_id}}}), (h:Character {{Name: 'Haymitch Abernathy'}})\n"
                        f"CREATE (c)-[:ALLY_OF]->(h);\n"
                    )
                else:
                    safe_alliance = alliance.replace("'", "`")
                    file.write(
                        f"MATCH (c:Character {{ID: {character_id}}}), (a:Alliance {{Name: '{safe_alliance}'}})\n"
                        f"CREATE (c)-[:BELONGS_TO]->(a);\n"
                    )

def create_neo4j_mentor_links(df, filename="cypher_files/link_characters_mentors.cypher"):
    with open(filename, "w", encoding="utf-8") as file:
        for _, row in df.iterrows():
            character_id = str(row["ID"])
            mentors = row.get("Mentor", None)

            if pd.isna(character_id) or pd.isna(mentors):
                continue

            mentor_list = [a.strip() for a in str(mentors).split(",")]
            for mentor in mentor_list:
                safe_mentor = mentor.replace("'", "`")
                file.write(
                    f"MATCH (c:Character {{ID: {character_id}}}), (m:Character {{Name: '{safe_mentor}'}})\n"
                    f"CREATE (m)-[:MENTOR]->(c);\n"
                )

# -------------------------------------------------------------------------------------

print("------------------------")
print("---Programa principal---")
print("------------------------")

hgDF = importar_CSV(ruta_csv)
hgDF = hgDF.drop('Columna 1', axis=1)

hgDF['ID'] = hgDF.index

# Create the cypher files for creating nodes
districts = hgDF['District'].unique()
print("\nUnique values in 'District' column:", districts)
create_neo4j_district_nodes(districts)

games = hgDF['Game_Year'].unique()
print("\nUnique values in 'Game_Year' column:", games)
create_neo4j_game_year_nodes(games)

books = hgDF['Appearance'].unique()
print("\nUnique values in 'Appearance' column:", books)
create_neo4j_book_nodes(books)

alliances = hgDF['Alliance'].unique()
print("\nUnique values in 'Alliance' column:", alliances)
create_neo4j_alliance_nodes(alliances)

create_neo4j_character_nodes(hgDF)

# Create the cypher files for linking
create_character_district_links(hgDF)
create_character_game_links(hgDF)
create_character_book_links(hgDF)
create_character_alliance_links(hgDF)
create_neo4j_mentor_links(hgDF)

consultar_atributos(hgDF)

print("----------------------")
print("---Fin del programa---")
print("----------------------")

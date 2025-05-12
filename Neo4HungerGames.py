from neo4j import GraphDatabase
import pandas as pd

class Neo4HungerGames:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def delete_all_nodes(self):
        with self.driver.session() as session:
            query = "MATCH (n) DELETE n"
            session.run(query)

    def get_next_character_id(self):
        with self.driver.session() as session:
            result = session.run("MATCH (c:Character) RETURN MAX(c.ID) AS max_id")
            max_id = result.single()["max_id"]
            return max_id + 1 if max_id is not None else 0

    def create_nodes_links_from_df(self, df):
        try:
            districts = df['District'].unique()
            self.create_neo4j_district_nodes(districts)

            games = df['Game_Year'].unique()
            self.create_neo4j_game_year_nodes(games)

            books = df['Appearance'].unique()
            self.create_neo4j_book_nodes(books)

            alliances = df['Alliance'].unique()
            self.create_neo4j_alliance_nodes(alliances)

            self.create_neo4j_character_nodes(df)

            self.create_neo4j_death_nodes(df)

            # Create the cypher files for linking
            self.create_character_district_links(df)
            self.create_character_game_links(df)
            self.create_character_book_links(df)
            self.create_character_alliance_links(df)
            self.create_neo4j_mentor_links(df)
            self.create_neo4j_death_links(df)
        finally:
            self.close()

    def create_neo4j_district_nodes(self, values):
        with self.driver.session() as session:
            for val in values:
                if val != 0:
                    session.run(f"CREATE (:District {{Name: 'District {val}', Number: {val}}});\n")
                elif val == 0:
                    session.run(f"CREATE (:District {{Name: 'The Capitol', Number: {val}}});\n")
                else:
                    session.run(f"CREATE (:District {{Name: '???', Number: -1}});\n")

    def create_neo4j_game_year_nodes(self, games):
        all_years = set()
        for val in games:
            if pd.isna(val):
                continue
            parts = [a.strip() for a in str(val).split(",")]
            all_years.update(parts)

        with self.driver.session() as session:
            for year in sorted(all_years):
                session.run(f"CREATE (:Game_Year {{Year: {year}}});\n")

    def create_neo4j_book_nodes(self, books):
        all_books = set()
        for val in books:
            if pd.isna(val):
                continue
            parts = [a.strip() for a in str(val).split(",")]
            all_books.update(parts)

        with self.driver.session() as session:
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
                    session.run(f"CREATE (:Book {{Title: '{safe_name}', Order: '{order}'}});\n")

    def create_neo4j_alliance_nodes(self, alliances):
        all_alliances = set()
        for val in alliances:
            if pd.isna(val):
                continue
            parts = [a.strip() for a in str(val).split(",")]
            all_alliances.update(parts)

        with self.driver.session() as session:
            for alliance in sorted(all_alliances):
                safe_name = alliance.replace("'", "`")
                if safe_name not in ["Katniss", "Haymitch"]:
                    session.run(f"CREATE (:Alliance {{Name: '{safe_name}'}});\n")

    def create_neo4j_character_nodes(self, df):
        allowed_columns = ["ID", "Name", "Gender", "Profession"]
        with self.driver.session() as session:
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
                session.run(f"CREATE (:Character {{{props}}});\n")

    def create_neo4j_character_node(self, character_data):
        allowed_columns = ["ID", "Name", "Gender", "Profession"]
        props_list = []

        with self.driver.session() as session:
            for col in allowed_columns:
                if col in character_data:
                    value = character_data[col]
                    if not value and col == "Profession":
                        value = "None"
                    if value:
                        safe_value = str(value).replace("'", "`")  # proteger apóstrofes
                        props_list.append(f"{col}: '{safe_value}'")

            props = ", ".join(props_list)
            session.run(f"CREATE (:Character {{{props}}});\n")
    
    def update_neo4j_character_node(self, data):
        with self.driver.session() as session:
            session.run(
                """
                MATCH (c:Character {ID: $ID})
                SET c.Name = $Name,
                    c.Gender = $Gender,
                    c.Profession = $Profession
                """,
                data
            )

    def delete_character_district_links(self, char_id):
        with self.driver.session() as session:
            session.run(
                """
                MATCH (c:Character {ID: $id})-[r:FROM_DISTRICT]->()
                DELETE r
                """,
                {"id": char_id}
            )

    def delete_neo4j_character_and_relationships(self, char_id):
        with self.driver.session() as session:
            session.run(
                """
                MATCH (c:Character {ID: $id})
                DETACH DELETE c
                """,
                {"id": char_id}
            )

    def create_neo4j_death_nodes(self, df):
        unique_deaths = set()
        with self.driver.session() as session:
            for _, row in df.iterrows():
                char_id = str(row["ID"])
                death = row.get("Killed by", None)
                if pd.isna(char_id) or pd.isna(death):
                    continue
                death_str = str(death).strip()
                if death_str not in unique_deaths:
                    unique_deaths.add(death_str)
                    safe_death = death_str.replace("'", "`")
                    session.run(f"CREATE (c:Death {{Name: '{safe_death}'}})\n")

    # -------------------------------------------------------------------------------------

    def create_character_district_links(self, df):
        with self.driver.session() as session:
            for _, row in df.iterrows():
                id = str(row["ID"])
                district = row["District"]

                if pd.isna(id) or pd.isna(district):
                    continue

                session.run(
                    f"MATCH (c:Character {{ID: '{id}'}}), (d:District {{Number: {int(district)}}})\n"
                    f"CREATE (c)-[:FROM_DISTRICT]->(d);\n"
                )

    def create_character_district_link(self, character_id, district_number):
        if not character_id or not district_number:
            return

        with self.driver.session() as session:
            session.run(
                """
                MATCH (c:Character {ID: $id}), (d:District {Number: $district})
                CREATE (c)-[:FROM_DISTRICT]->(d);
                """,
                {"id": character_id, "district": int(district_number)}
            )

    def create_character_game_links(self, df):
        with self.driver.session() as session:
            for _, row in df.iterrows():
                char_id = str(row["ID"])
                games = row.get("Game_Year", None)
                winner = str(row.get("Winner", "No")).strip().lower()

                if pd.isna(char_id) or pd.isna(games):
                    continue

                winner_flag = "true" if winner == "yes" else "false"

                years = [g.strip() for g in str(games).split(",")]

                for year in years:
                    if year.isdigit():
                        year_int = int(year)
                        if year_int == 75:
                            session.run(
                                f"MATCH (c:Character {{ID: '{char_id}'}}), (g:Game_Year {{Year: {year_int}}})\n"
                                f"CREATE (c)-[:PARTICIPATED_IN {{victor: false}}]->(g);\n"
                            )
                        else:
                            session.run(
                                f"MATCH (c:Character {{ID: '{char_id}'}}), (g:Game_Year {{Year: {year_int}}})\n"
                                f"CREATE (c)-[:PARTICIPATED_IN {{victor: {winner_flag}}}]->(g);\n"
                            )

    def create_character_book_links(self, df):
        trilogy_books = ["The Hunger Games", "Catching Fire", "Mockingjay"]

        with self.driver.session() as session:
            for _, row in df.iterrows():
                char_id = str(row["ID"])
                books = row.get("Appearance", None)

                if pd.isna(char_id) or pd.isna(books):
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
                        session.run(
                            f"MATCH (c:Character {{ID: '{char_id}'}}), (b:Book {{Title: '{safe_book}'}})\n"
                            f"CREATE (c)-[:APPEARS_IN]->(b);\n"
                        )

    def create_character_alliance_links(self, df):
        with self.driver.session() as session:
            for _, row in df.iterrows():
                char_id = str(row["ID"])
                alliances = row.get("Alliance", None)

                if pd.isna(char_id) or pd.isna(alliances):
                    continue

                alliance_list = [a.strip() for a in str(alliances).split(",")]

                for alliance in alliance_list:
                    if alliance == "Katniss":
                        session.run(
                            f"MATCH (c:Character {{ID: '{char_id}'}}), (k:Character {{Name: 'Katniss Everdeen'}})\n"
                            f"CREATE (c)-[:ALLY_OF]->(k);\n"
                        )
                    elif alliance == "Haymitch":
                        session.run(
                            f"MATCH (c:Character {{ID: '{char_id}'}}), (h:Character {{Name: 'Haymitch Abernathy'}})\n"
                            f"CREATE (c)-[:ALLY_OF]->(h);\n"
                        )
                    else:
                        safe_alliance = alliance.replace("'", "`")
                        session.run(
                            f"MATCH (c:Character {{ID: '{char_id}'}}), (a:Alliance {{Name: '{safe_alliance}'}})\n"
                            f"CREATE (c)-[:BELONGS_TO]->(a);\n"
                        )

    def create_neo4j_mentor_links(self, df):
        with self.driver.session() as session:
            for _, row in df.iterrows():
                char_id = str(row["ID"])
                mentors = row.get("Mentor", None)

                if pd.isna(char_id) or pd.isna(mentors):
                    continue

                mentor_list = [a.strip() for a in str(mentors).split(",")]
                for mentor in mentor_list:
                    safe_mentor = mentor.replace("'", "`")
                    session.run(
                        f"MATCH (c:Character {{ID: '{char_id}'}}), (m:Character {{Name: '{safe_mentor}'}})\n"
                        f"CREATE (m)-[:MENTORS]->(c);\n"
                    )

    def create_neo4j_death_links(self, df):
        with self.driver.session() as session:
            for _, row in df.iterrows():
                char_id = str(row["ID"])
                death = row.get("Killed by", None)

                if pd.isna(char_id) or pd.isna(death):
                    continue

                death_str = str(death).strip()

                result = session.run(
                    "MATCH (killer:Character {Name: $name}) RETURN killer LIMIT 1",
                    name=death_str
                )
                killer_node = result.single()

                if killer_node:
                    session.run(
                        "MATCH (c:Character {ID: $char_id}), (k:Character {Name: $killer_name}) "
                        "CREATE (k)-[:KILLED]->(c)",
                        char_id=char_id,
                        killer_name=death_str
                    )
                else:
                    session.run(
                        "MATCH (c:Character {ID: $char_id}), (d:Death {Name: $death_name}) "
                        "CREATE (c)-[:DIED_BY]->(d)",
                        char_id=char_id,
                        death_name=death_str
                    )

    def create_family_links(self, id1, id2):
        with self.driver.session() as session:
                session.run(
                    f"MATCH (a:Character {{ID: '{id1}'}}), (b:Character {{ID: '{id2}'}})\n"
                    f"CREATE (a)-[:FAMILY]->(b);\n"
                )

    # -------------------------------------------------------------------------------------

    def get_all_characters(self):
        with self.driver.session() as session:
            result = session.run("""
                MATCH (c:Character)
                OPTIONAL MATCH (c)-[:FROM_DISTRICT]->(d:District)
                RETURN DISTINCT c.ID AS id,
                                c.Name AS name,
                                c.Gender AS gender,
                                c.Profession AS profession,
                                d.Name AS district_name
                ORDER BY name
            """)
            characters = []
            seen_ids = set()
            for record in result:
                if record["id"] not in seen_ids:
                    characters.append({
                        "id": record["id"],
                        "name": record["name"],
                        "gender": record["gender"],
                        "profession": record["profession"],
                        "district": record["district_name"] or "Sin distrito"
                    })
                    seen_ids.add(record["id"])
            return characters
    
    def get_character_by_id(self, char_id):
        with self.driver.session() as session:
            result = session.run(
                """
                MATCH (c:Character {ID: $id})
                OPTIONAL MATCH (c)-[:FROM_DISTRICT]->(d:District)
                RETURN c.ID AS id,
                    c.Name AS name,
                    c.Gender AS gender,
                    c.Profession AS profession,
                    d.Number AS district_number
                """,
                {"id": char_id}
            )
            record = result.single()
            if record:
                return {
                    "id": record["id"],
                    "name": record["name"],
                    "gender": record["gender"],
                    "profession": record["profession"],
                    "district": record["district_number"]  # Puede ser None
                }
            else: return None


    def get_all_districts(self):
        with self.driver.session() as session:
            result = session.run("MATCH (d:District) RETURN DISTINCT d.Name AS name, d.Number AS number")
            return [
                {
                    "name": record["name"],
                    "number": record["number"]
                }
                for record in result
            ]
        
    def get_all_games(self):
        with self.driver.session() as session:
            result = session.run("MATCH (g:Game_Year) RETURN DISTINCT g.Year AS year ORDER BY year")
            return [{"year": record["year"]} for record in result]

from neo4j import GraphDatabase
from Neo4Dataframes import relationship_weights

class Neo4HungerGames:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
    def close(self):
        self.driver.close()

    def delete_all_links_and_nodes(self):
        with self.driver.session() as session:
            query = "MATCH (n)-[r]-() DELETE r, n"
            session.run(query)
            query = "MATCH (n) DELETE n"
            session.run(query)

    def get_next_character_id(self):
        with self.driver.session() as session:
            result = session.run("MATCH (c:Character) RETURN MAX(c.ID) AS max_id")
            max_id = result.single()["max_id"]
            if max_id is None:
                max_id = 0
            else:
                max_id = int(max_id)
                max_id += 1
            return str(max_id)

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

    def delete_character_district_links(self, character_id):
        with self.driver.session() as session:
            session.run(
                """
                MATCH (c:Character {ID: $id})-[r:FROM_DISTRICT]->()
                DELETE r
                """,
                {"id": character_id}
            )

    def delete_neo4j_character_and_relationships(self, character_id):
        with self.driver.session() as session:
            session.run(
                """
                MATCH (c:Character {ID: $id})
                DETACH DELETE c
                """,
                {"id": int(character_id)}
            )

    def update_neo4j_character_node(self, data):
        with self.driver.session() as session:
            session.run(
                """
                MATCH (c:Character {ID: $ID})
                SET c.Name = $Name,
                    c.Gender = $Gender,
                    c.Profession = $Profession
                """,
                {
                    "ID": int(data["ID"]),
                    "Name": data["Name"],
                    "Gender": data["Gender"],
                    "Profession": data["Profession"]
                }
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

    def create_family_links(self, id1, id2, relationship_type):
        with self.driver.session() as session:
            session.run(
                """
                MATCH (a:Character {ID: $id1}), (b:Character {ID: $id2})
                CREATE (a)-[r:FAMILY {type: $type} {weight: $weight}]->(b)
                """,
                {"id1": int(id1), "id2": int(id2), "type": relationship_type.upper(), "weight": relationship_weights["FAMILY"]}
            )

    # -------------------------------------------------------------------------------------

    def get_all_characters_id_and_name(self):
        with self.driver.session() as session:
            result = session.run("MATCH (c:Character) RETURN c.ID AS id, c.Name AS name ORDER BY c.ID")
            return [{"id": record["id"], "name": record["name"]} for record in result]


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
    
    def get_character_by_id(self, character_id):
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
                {"id": character_id}
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

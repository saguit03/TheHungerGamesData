from neo4j import GraphDatabase
from Neo4Dataframes import relationship_weights

class Neo4HungerGames:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
    def close(self):
        self.driver.close()

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
        # Diccionario de pesos por tipo de relación
        weights = {
            "LOVER": 0.1,
            "SIBLING": 0.5,
            "PARENT": 0.5,
            "CHILD": 0.5,
            "COUSIN": 1.0,
            "FRIEND": 0.3,
            "OTHER": 1.0
        }

        rel_type = relationship_type.upper()
        weight = weights.get(rel_type, 1.0)  # Valor por defecto si no se encuentra

        with self.driver.session() as session:
            session.run(
                """
                MATCH (a:Character {ID: $id1}), (b:Character {ID: $id2})
                CREATE (a)-[r:FAMILY {type: $type, weight: $weight}]->(b)
                """,
                {
                    "id1": int(id1),
                    "id2": int(id2),
                    "type": rel_type,
                    "weight": weight
                }
            )

    def get_all_family_links(self):
        with self.driver.session() as session:
            result = session.run(
                """
                MATCH (a:Character)-[r:FAMILY]->(b:Character)
                RETURN a.ID AS source_id, a.Name AS source_name,
                    b.ID AS target_id, b.Name AS target_name,
                    r.type AS type, r.weight AS weight
                """
            )
            return [record.data() for record in result]
        

    def delete_family_link(self, id1, id2, relationship_type):
        with self.driver.session() as session:
            session.run(
                """
                MATCH (a:Character {ID: $id1})-[r:FAMILY {type: $type}]->(b:Character {ID: $id2})
                DELETE r
                """,
                {"id1": id1, "id2": id2, "type": relationship_type}
            )


    def get_all_relationships(self):
        with self.driver.session() as session:
            result = session.run(
                """
                MATCH (a)-[r]->(b)
                RETURN a.ID AS source_id,  coalesce(a.Name, a.ID) AS source, labels(a)[0] AS source_label,
                    b.ID AS target_id, coalesce(b.Name, b.ID) AS target, labels(b)[0] AS target_label,
                    type(r) AS rel_type, coalesce(r.weight, 15.0) AS weight
                """
            )
            return [record.data() for record in result]

    def delete_relationship(self, source_id, source_label, target_id, target_label, rel_type):
        with self.driver.session() as session:
            query = f"""
                MATCH (a:{source_label} {{ID: $source_id}})-[r:{rel_type}]->(b:{target_label} {{ID: $target_id}})
                DELETE r
            """
            print(query)
            session.run(
                query,
                {
                    "source_id": int(source_id),
                    "target_id": int(target_id)
                }
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
            result = session.run("MATCH (d:District) RETURN DISTINCT d.ID as id, d.Name AS name, d.Number AS number")
            return [
                {
                    "id": record["id"],
                    "name": record["name"],
                    "number": record["number"]
                }
                for record in result
            ]
    
    def get_all_books(self):
        with self.driver.session() as session:
            result = session.run("MATCH (b:Book) RETURN DISTINCT b.ID as id, b.Order AS order, b.Title AS title")
            return [
                {
                    "id": record["id"],
                    "order": record["order"],
                    "title": record["title"]
                }
                for record in result
            ]
        
        
    def get_all_games(self):
        with self.driver.session() as session:
            result = session.run("MATCH (g:Game_Year) RETURN DISTINCT g.ID as id, g.Year AS year ORDER BY year")
            return [
                {
                "id": record["id"],
                "year": record["year"]
                } 
                for record in result
                ]
        
    def get_all_alliances(self):
        with self.driver.session() as session:
            result = session.run("MATCH (a:Alliance) RETURN DISTINCT a.ID as id, a.Name AS name")
            return [
                {
                    "id": record["id"],
                    "name": record["name"]
                }
                for record in result
            ]

    def get_character_counts_per_book(self):
        with self.driver.session() as session:
            result = session.run("""
                MATCH (c:Character)-[:APPEARS_IN]->(b:Book)
                RETURN b.Title AS title, count(c) AS character_count
                ORDER BY character_count DESC
            """)
            return [
                {
                    "title": record["title"],
                    "count": record["character_count"]
                }
                for record in result
            ]

    def get_character_counts_per_district(self):
        with self.driver.session() as session:
            result = session.run("""
                MATCH (c:Character)-[:FROM_DISTRICT]->(d:District)
                RETURN d.Name AS district, count(c) AS character_count
                ORDER BY character_count DESC
            """)
            return [
                {
                    "district": record["district"],
                    "count": record["character_count"]
                }
                for record in result
            ]
        
    def get_character_counts_per_alliance(self):
        with self.driver.session() as session:
            result = session.run("""
                MATCH (c:Character)-[:ALLY_OF|:BELONGS_TO]->(a:Character|Alliance)
                RETURN a.Name AS alliance, count(c) AS character_count
                ORDER BY character_count DESC
            """)
            return [
                {
                    "alliance": record["alliance"],
                    "count": record["character_count"]
                }
                for record in result
            ]
        
    def get_character_counts_per_game(self):
        with self.driver.session() as session:
            result = session.run("""
                MATCH (p:Character)-[:PARTICIPATED_IN]->(g:Game_Year)
                OPTIONAL MATCH (p)-[:MENTORED_BY]->(m:Character)
                RETURN g.Year AS game_year,
                    count(DISTINCT p.Name) AS participants,
                    count(DISTINCT m.Name) AS mentors
                ORDER BY game_year DESC
            """)
            return [
                {
                    "game": record["game_year"],
                    "count": record["participants"]+record["mentors"]
                }
                for record in result
            ]
        
    def get_count_kills_per_cause(self):
        with self.driver.session() as session:
            result = session.run("""
                MATCH (p)-[:KILLED]->(k:Character)
                RETURN p.Name AS killer, count(DISTINCT k.Name) AS killed
                ORDER BY killed DESC
            """)
            return [
                {
                    "killer": record["killer"],
                    "killed": record["killed"]
                }
                for record in result
            ]

    def get_characters_from_other_books(self, title):
        with self.driver.session() as session:
            result = session.run(
                """
                MATCH (c:Character)-[:APPEARS_IN]->(b:Book {Title: $title})
                MATCH (c)-[:APPEARS_IN]->(otherBook:Book)
                WHERE otherBook.Title <> $title
                RETURN DISTINCT c.Name AS name, collect(DISTINCT otherBook.Title) AS other_books
                ORDER BY name
                """,
                {"title": title}
            )
            characters = []
            for record in result:
                characters.append({
                    "name": record["name"],
                    "other_books": record["other_books"]
                })
            return characters

    def get_characters_from_a_book(self, title):
        with self.driver.session() as session:
            result = session.run(
                """
                MATCH (c:Character)-[:APPEARS_IN]->(b:Book {Title: $title})
                RETURN DISTINCT c.Name AS name
                ORDER BY name
                """,
                {"title": title}
            )
            characters = []
            for record in result:
                characters.append({
                    "name": record["name"],
                })
            return characters
        
    def get_dead_characters_from_a_cause(self, cause):
        with self.driver.session() as session:
            result = session.run(
                """
                MATCH (p {Name: $cause})-[:KILLED]->(k:Character)
                RETURN DISTINCT k.Name AS name
                ORDER BY name
                """,
                {"cause": cause}
            )
            characters = []
            for record in result:
                characters.append({
                    "name": record["name"],
                })
            return characters

    def get_max_death_cause(self):
        with self.driver.session() as session:
            result = session.run("""
                MATCH (p)-[:KILLED]->(k:Character)
                RETURN p.Name AS killer, count(DISTINCT k.Name) as killed, collect(DISTINCT k.Name) AS victims
                ORDER BY killed DESC
                LIMIT 1
            """)
            return [
                {
                    "killer": record["killer"],
                    "killed": record["killed"],
                    "victims": record["victims"]
                }
                for record in result
            ]
        
    def get_max_appearances(self):
        with self.driver.session() as session:
            result = session.run("""
                MATCH (c:Character)-[:APPEARS_IN]->(b:Book)
                RETURN c.Name AS character, count(b) AS appearances
                ORDER BY appearances DESC
                LIMIT 1
            """)
            return [
                {
                    "character": record["character"],
                    "appearances": record["appearances"]
                }
                for record in result
            ]
        
    def get_population_per_district_in_books(self):
        with self.driver.session() as session:
            result = session.run("""
                MATCH (c:Character)-[:FROM_DISTRICT]->(d:District),
                (c)-[:APPEARS_IN]->(b:Book)
                RETURN b.Title AS title, b.Order as order, d.Name AS district, count(DISTINCT c) AS characterCount
                ORDER BY b.Order, district
            """)
            return [
                {
                    "title": record["title"],
                    "order": record["order"],
                    "district": record["district"],
                    "characterCount": record["characterCount"]
                }
                for record in result
            ]
        
    def get_mentors_with_victorious_tributes(self):
        with self.driver.session() as session:
            result = session.run(
                """
                MATCH (mentor:Character)-[:MENTORS]->(tribute:Character)-[p:PARTICIPATED_IN]->(game:Game_Year)
                WHERE p.victor = true OR p.victor = "true"
                RETURN mentor, 
                    collect(DISTINCT tribute) AS victoriousTributes, 
                    collect(DISTINCT game) AS winningGames, 
                    count(DISTINCT tribute) AS victories
                """
            )
            mentors = []
            for record in result:
                mentor = dict(record["mentor"])
                mentor["victorious_tributes"] = [dict(t) for t in record["victoriousTributes"]]
                mentor["winning_games"] = [dict(g) for g in record["winningGames"]]
                mentor["victories"] = record["victories"]
                mentors.append(mentor)

            return mentors
            
    def get_characters_and_their_known_people_from_other_districts(self):
        with self.driver.session() as session:
            # [*..1] busca cualquier relación de distancia 1
            # entre dos nodos, sin importar el tipo de relación
            result = session.run(
                """
                MATCH (c:Character)-[*..1]-(other:Character)
                MATCH (c)-[:FROM_DISTRICT]->(dc:District)
                MATCH (other)-[:FROM_DISTRICT]->(do:District)
                WHERE c.ID <> other.ID AND dc.Name <> do.Name
                WITH c.Name AS characterName,
                    collect(DISTINCT do.Name) AS knownDistricts,
                    collect(DISTINCT {name: other.Name, district: do.Name}) AS knownPeople,
                    count(DISTINCT other) AS peopleKnown
                ORDER BY peopleKnown DESC
                LIMIT 5
                RETURN characterName, knownDistricts, knownPeople
                """
            )
            characters = []
            for record in result:
                characters.append({
                    "name": record["characterName"],
                    "knownDistricts": record["knownDistricts"],
                    "knownPeople": record["knownPeople"]
                })
            return characters

    def get_game_with_most_involved_characters(self):
        with self.driver.session() as session:
            result = session.run(
                """
                MATCH (g:Game_Year)
                OPTIONAL MATCH (p:Character)-[:PARTICIPATED_IN]->(g)
                OPTIONAL MATCH (m:Character)-[:MENTORS]->(p)
                WITH g, collect(DISTINCT p) + collect(DISTINCT m) AS allCharacters
                WITH g, allCharacters, size(allCharacters) AS totalPeople
                ORDER BY totalPeople DESC
                LIMIT 1
                UNWIND allCharacters AS c
                OPTIONAL MATCH (c)-[r]-(related:Character)
                RETURN g.Year AS gameYear,
                    collect(DISTINCT c.Name) AS involvedCharacters,
                    collect(DISTINCT {from: c.Name, type: type(r), to: related.Name}) AS relationships
                """
            )
            record = result.single()
            if not record:
                return {}

            return {
                "gameYear": record["gameYear"],
                "characters": record["involvedCharacters"],
                "relationships": record["relationships"]
            }
        
    def get_game_with_most_involved_characters_detailed(self):
        with self.driver.session() as session:
            result = session.run("""
                MATCH (g:Game_Year)
                OPTIONAL MATCH (p:Character)-[part:PARTICIPATED_IN]->(g)
                OPTIONAL MATCH (m:Character)-[:MENTORS]->(p)
                WITH g, 
                    collect(DISTINCT p) + collect(DISTINCT m) AS allCharacters, 
                    collect(DISTINCT part) AS parts
                WITH g, allCharacters, size(allCharacters) AS totalPeople
                ORDER BY totalPeople DESC
                LIMIT 1
                WITH g
                MATCH (p:Character)-[part:PARTICIPATED_IN]->(g)
                OPTIONAL MATCH (m:Character)-[:MENTORS]->(p)
                RETURN g.Year AS gameYear,
                    collect(DISTINCT {name: p.Name, victor: part.victor}) AS tributes,
                    collect(DISTINCT {name: m.Name, protege: p.Name, protegeVictor: part.victor}) AS mentors
            """)
            record = result.single()
            if not record:
                return {}
            
            # Eliminar tributos y mentores cuyo nombre esté a null
            tributes = [t for t in record["tributes"] if t["name"] is not None]
            mentors = [m for m in record["mentors"] if m["name"] is not None]
            return {
                "gameYear": record["gameYear"],
                "tributes": tributes,
                "number_of_tributes": len(tributes),
                "mentors": mentors,
                "number_of_mentors": len(mentors),
            }



    def shortest_path(self, source_id, target_id):
        with self.driver.session() as session:
            result = session.run(
                """
                MATCH p = shortestPath((a:Character {ID: $source_id})-[*]-(b:Character {ID: $target_id}))
                RETURN p
                """,
                {"source_id": int(source_id), "target_id": int(target_id)}
            )

            for record in result:
                path = record["p"]
                path_data = []

                # Recorrer nodos y relaciones como secuencia
                for i in range(len(path.relationships)):
                    start_node = path.nodes[i]
                    end_node = path.nodes[i + 1]
                    rel = path.relationships[i]

                    start_name = start_node.get("Name", f"ID {start_node['ID']}")
                    end_name = end_node.get("Name", f"ID {end_node['ID']}")
                    rel_type = rel.type

                    path_data.append((start_name, rel_type, end_name))

                return path_data

            # Si no se encontró camino
            return []

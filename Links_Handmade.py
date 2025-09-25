from neo4j import GraphDatabase
from Link_Weights import relationship_weights


def handmake_links(driver: GraphDatabase.driver):
    weight = relationship_weights["HANDMADE"]
    with driver.session() as session:
        session.run(
            f"""
            MATCH (c:Character {{Name:"Coriolanus Snow"}}), (g:Game_Year)
            WHERE g.Year > 10
            MERGE (c)-[:CONTROLS {{weight: $weight}}]->(g)
            """, weight=weight)
        session.run(
            f"""
            MATCH (c:Character {{Name:"Volumnia Gaul"}}), (g:Game_Year)
            WHERE g.Year < 11
            MERGE (c)-[:CONTROLS {{weight: $weight}}]->(g)
            """, weight=weight)
        session.run(
            f"""
            MATCH (c:Character {{Name:"Coriolanus Snow"}}), (d:District {{ID:0}})
            MERGE (c)-[:GOVERNS {{weight: $weight}}]->(d)
            """, weight=weight)
        session.run(
            f"""
            MATCH (c:District {{ID:0}}), (dt:District)
            WHERE dt.ID > 0 AND dt.ID < 13
            MERGE (c)-[:GOVERNS {{weight: $weight}}]->(dt)
            """, weight=weight)            
        
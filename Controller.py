import uuid
from flask import Flask, render_template, redirect, url_for, session, request
from Neo4HungerGames import Neo4HungerGames

class Controller:
    @staticmethod
    def create_character(connection: Neo4HungerGames, request):
        char_id = connection.get_next_character_id()

        character_data = {
            "ID": char_id,
            "Name": request.form.get("name"),
            "Gender": request.form.get("gender"),
            "Profession": request.form.get("profession")
        }
        district_number = request.form.get("district")

        connection.create_neo4j_character_node(character_data)

        if district_number:
            connection.create_character_district_link(char_id, district_number)
        return redirect("/characters/all")
    
    @staticmethod
    def update_character(connection: Neo4HungerGames, request, char_id):
        if request.method == "GET":
            # Obtener datos del personaje
            character = connection.get_character_by_id(char_id)
            districts = connection.get_all_districts()
            return render_template("update_character.html", character=character, districts=districts)
        else:
        # Recoger nuevos datos del formulario
            updated_data = {
                "ID": char_id,
                "Name": request.form.get("name"),
                "Gender": request.form.get("gender"),
                "Profession": request.form.get("profession")
            }
            district_number = request.form.get("district")

            # Actualizar nodo del personaje
            connection.update_neo4j_character_node(updated_data)

            # Eliminar relaciones anteriores y crear la nueva si se indica
            connection.delete_character_district_links(char_id)
            if district_number:
                connection.create_character_district_link(char_id, district_number)

            return redirect("/characters/all")
    
    @staticmethod
    def delete_character(connection: Neo4HungerGames, request):
        
        char_id = request.form.get("character_id")
        connection.delete_neo4j_character_and_relationships(char_id)
        return redirect("/characters/all")

    @staticmethod
    def link_character_game(connection: Neo4HungerGames, request):
        if request.method == "GET":
            # GET method: render form with available years
            games = connection.get_all_games()
            return render_template("link_character_game.html", games=games)
        
        char_id = request.form.get("character_id").strip()
        game_year = request.form.get("game_year").strip()
        winner = request.form.get("winner").strip().lower()

        if not char_id or not game_year:
            return "Faltan campos obligatorios", 400

        winner_flag = "true" if winner == "yes" else "false"

        with connection.driver.session() as session:
            if game_year == "75":
                session.run(
                    f"MATCH (c:Character {{ID: '{char_id}'}}), (g:Game_Year {{Year: 75}})\n"
                    f"CREATE (c)-[:PARTICIPATED_IN {{victor: false}}]->(g);"
                )
            else:
                session.run(
                    f"MATCH (c:Character {{ID: '{char_id}'}}), (g:Game_Year {{Year: {int(game_year)}}})\n"
                    f"CREATE (c)-[:PARTICIPATED_IN {{victor: {winner_flag}}}]->(g);"
                )
        return redirect("/characters/all")

    

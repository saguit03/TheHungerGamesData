import uuid
from flask import Flask, render_template, redirect, url_for, session, request
from Neo4HungerGames import Neo4HungerGames

class Controller:
    @staticmethod
    def create_character(connection: Neo4HungerGames, request):
        character_id = connection.get_next_character_id()

        character_data = {
            "ID": character_id,
            "Name": request.form.get("name"),
            "Gender": request.form.get("gender"),
            "Profession": request.form.get("profession")
        }
        district_number = request.form.get("district")

        connection.create_neo4j_character_node(character_data)

        if district_number:
            connection.create_character_district_link(character_id, district_number)
        print(character_data)
        return redirect("/characters/all")
    
    @staticmethod
    def update_character(connection: Neo4HungerGames, request, character_id):
        if request.method == "GET":
            # Obtener datos del personaje
            character = connection.get_character_by_id(character_id)
            districts = connection.get_all_districts()
            return render_template("update_character.html", character=character, districts=districts)
        else:
        # Recoger nuevos datos del formulario
            updated_data = {
                "ID": character_id,
                "Name": request.form.get("name"),
                "Gender": request.form.get("gender"),
                "Profession": request.form.get("profession")
            }
            district_number = request.form.get("district")

            # Actualizar nodo del personaje
            connection.update_neo4j_character_node(updated_data)

            # Eliminar relaciones anteriores y crear la nueva si se indica
            connection.delete_character_district_links(character_id)
            if district_number:
                connection.create_character_district_link(character_id, district_number)

            return redirect("/characters/all")
    
    @staticmethod
    def delete_character(connection: Neo4HungerGames, request):
        character_id = request.form.get("character_id")
        connection.delete_neo4j_character_and_relationships(character_id)
        return redirect("/characters")
    
    @staticmethod
    def delete_character_by_id(connection: Neo4HungerGames, character_id):
        print("Eliminando personaje con ID:", character_id)
        connection.delete_neo4j_character_and_relationships(character_id)
        return redirect("/characters/all")

    @staticmethod
    def update_character(connection: Neo4HungerGames, request, character_id):
        character_data = {
            "ID": int(character_id),
            "Name": request.form.get("name"),
            "Gender": request.form.get("gender"),
            "Profession": request.form.get("profession")
        }
        connection.update_neo4j_character_node(character_data)
        return redirect("/characters/all")

    @staticmethod
    def link_character_game(connection: Neo4HungerGames, request):
        if request.method == "GET":
            # GET method: render form with available years
            games = connection.get_all_games()
            return render_template("link_character_game.html", games=games)
        
        character_id = request.form.get("character_id").strip()
        game_year = request.form.get("game_year").strip()
        winner = request.form.get("winner").strip().lower()

        if not character_id or not game_year:
            return "Faltan campos obligatorios", 400

        winner_flag = "true" if winner == "yes" else "false"

        with connection.driver.session() as session:
            if game_year == "75":
                session.run(
                    f"MATCH (c:Character {{ID: {character_id}}}), (g:Game_Year {{Year: 75}})\n"
                    f"CREATE (c)-[:PARTICIPATED_IN {{victor: false}}]->(g);"
                )
            else:
                session.run(
                    f"MATCH (c:Character {{ID: {character_id}}}), (g:Game_Year {{Year: {int(game_year)}}})\n"
                    f"CREATE (c)-[:PARTICIPATED_IN {{victor: {winner_flag}}}]->(g);"
                )
        return redirect("/characters/all")

    @staticmethod
    def create_family_link(connection: Neo4HungerGames, request):
        id1 = request.form.get("id1")
        id2 = request.form.get("id2")
        relationship_type = request.form.get("relationship_type")

        if id1 == id2:
            return "No se puede vincular un personaje consigo mismo.", 400
        
        if not id1 or not id2:
            return "Faltan datos", 400

        try:
            connection.create_family_links(int(id1), int(id2),relationship_type)
            return redirect("/characters")
        except Exception as e:
            print("Error creando vínculo familiar:", e)
            return f"Error: {str(e)}", 500



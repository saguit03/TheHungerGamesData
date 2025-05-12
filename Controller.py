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
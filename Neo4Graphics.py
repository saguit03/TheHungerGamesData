from Neo4HungerGames import Neo4HungerGames
from flask import Response
import io
import pandas as pd
import matplotlib.pyplot as plt

class Neo4Graphics:
    def __init__(self, connection: Neo4HungerGames):
        self.connection = connection

    def characters_per_book(self):
        book_data = self.connection.get_character_counts_per_book()
        titles = [entry["title"] for entry in book_data]
        counts = [entry["count"] for entry in book_data]
        plt.figure(figsize=(10, 6))
        plt.bar(titles, counts, color='skyblue', edgecolor='black')
        plt.title('Número de personajes por libro')
        plt.xlabel('Libro')
        plt.ylabel('Cantidad de personajes')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        img = io.BytesIO()
        plt.savefig(img, format='png')
        plt.close()
        img.seek(0)
        return Response(img.getvalue(), mimetype='image/png')


    def characters_per_district(self):
        district_data = self.connection.get_character_counts_per_district()
        districts = [entry["district"] for entry in district_data]
        counts = [entry["count"] for entry in district_data]
        plt.figure(figsize=(10, 6))
        plt.bar(districts, counts, color='salmon', edgecolor='black')
        plt.title('Número de personajes por libro')
        plt.xlabel('Libro')
        plt.ylabel('Cantidad de personajes')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        img = io.BytesIO()
        plt.savefig(img, format='png')
        plt.close()
        img.seek(0)
        return Response(img.getvalue(), mimetype='image/png')

    def characters_per_alliance(self):
        alliance_data = self.connection.get_character_counts_per_alliance()
        alliances = [entry["alliance"] for entry in alliance_data]
        counts = [entry["count"] for entry in alliance_data]
        plt.figure(figsize=(10, 6))
        plt.bar(alliances, counts, color='lightgreen', edgecolor='black')
        plt.title('Número de personajes por alianza')
        plt.xlabel('Alianza')
        plt.ylabel('Cantidad de personajes')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        img = io.BytesIO()
        plt.savefig(img, format='png')
        plt.close()
        img.seek(0)
        return Response(img.getvalue(), mimetype='image/png')

    def characters_per_game(self):
        game_data = self.connection.get_character_counts_per_game()
        games = [entry["game"] for entry in game_data]
        counts = [entry["count"] for entry in game_data]
        plt.figure(figsize=(10, 6))
        plt.bar(games, counts, color='lightcoral', edgecolor='black')
        plt.title('Número de personajes por juego')
        plt.xlabel('Juego')
        plt.ylabel('Cantidad de personajes')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        img = io.BytesIO()
        plt.savefig(img, format='png')
        plt.close()
        img.seek(0)
        return Response(img.getvalue(), mimetype='image/png')

    def kills_per_cause(self):
        cause_data = self.connection.get_count_kills_per_cause()
        causes = [entry["killer"] for entry in cause_data]
        counts = [entry["killed"] for entry in cause_data]
        plt.figure(figsize=(10, 6))
        plt.bar(causes, counts, color='lightblue', edgecolor='black')
        plt.title('Número de muertes por causa')
        plt.xlabel('Causa de muerte')
        plt.ylabel('Cantidad de muertes')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        img = io.BytesIO()
        plt.savefig(img, format='png')
        plt.close()
        img.seek(0)
        return Response(img.getvalue(), mimetype='image/png')



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
        plt.figure(figsize=(8, 8))
        plt.pie(counts, labels=titles, autopct='%1.1f%%', startangle=140)
        plt.title('Distribución de personajes por libro')
        plt.axis('equal')  # Para que el círculo no salga ovalado
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
        plt.figure(figsize=(8, 8))
        plt.pie(counts, labels=districts, autopct='%1.1f%%', startangle=140)
        plt.title('Distribución de personajes por distrito')
        plt.axis('equal')
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

    def bubble_chart_districts_per_book(self):
        data = self.connection.get_population_per_district_in_books()
        df = pd.DataFrame(data)

        book_titles = df.sort_values(by="order")["title"].unique()
        districts = sorted(df["district"].unique())

        book_map = {title: idx for idx, title in enumerate(book_titles)}
        district_map = {district: idx for idx, district in enumerate(districts)}

        df["book_idx"] = df["title"].map(book_map)
        df["district_idx"] = df["district"].map(district_map)

        plt.figure(figsize=(12, 8))
        scatter = plt.scatter(
            df["book_idx"], df["district_idx"], 
            s=df["characterCount"] * 50,  # Escalar tamaño de burbuja
            alpha=0.6, c=df["characterCount"], cmap='viridis', edgecolors='w', linewidths=0.5
        )

        plt.xticks(ticks=list(book_map.values()), labels=book_titles, rotation=45, ha='right')
        plt.yticks(ticks=list(district_map.values()), labels=districts)
        plt.xlabel("Libro")
        plt.ylabel("Distrito")
        plt.title("Distribución de personajes por distrito en cada libro")

        cbar = plt.colorbar(scatter)
        cbar.set_label("Número de personajes")

        plt.tight_layout()
        img = io.BytesIO()
        plt.savefig(img, format='png')
        plt.close()
        img.seek(0)
        return Response(img.getvalue(), mimetype='image/png')


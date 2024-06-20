import requests
import mysql.connector
from mysql.connector import Error

API_KEY = ''  # Replace with actual API key
BASE_URL = 'http://www.omdbapi.com/'
database_name = 'movie_metadata'
table_name = 'movies'

def fetch_movie_metadata(movie_title):
    params = {
        'apikey': API_KEY,
        't': movie_title
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def enrich_metadata(metadata):
    if metadata:
        metadata['enriched'] = True
        metadata['custom_field'] = 'Example'
    return metadata

def store_metadata(metadata):
    try:
        connection = mysql.connector.connect(
            host='',
            database='',
            user='',
            password=''
        )
        if connection.is_connected():
            cursor = connection.cursor()
            insert_query = f"""
            INSERT INTO {table_name} (title, year, genre, director, enriched, custom_field, actors, plot, language, country)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(insert_query, (
                metadata.get('Title'),
                metadata.get('Year'),
                metadata.get('Genre'),
                metadata.get('Director'),
                metadata.get('enriched'),
                metadata.get('custom_field'),
                metadata.get('Actors'),
                metadata.get('Plot'),
                metadata.get('Language'),
                metadata.get('Country')
            ))
            connection.commit()
            print(f'Added metadata in {table_name} table in {database_name} db for {metadata.get("Title")}')
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    movie_titles = ['Up', 'Toy Story', 'Coco']
    for movie_title in movie_titles:
        metadata = fetch_movie_metadata(movie_title)
        if metadata and metadata.get('Response') == 'True':
            enriched_metadata = enrich_metadata(metadata)
            store_metadata(enriched_metadata)
        else:
            print(f'Failed to fetch metadata or movie not found: {movie_title}')

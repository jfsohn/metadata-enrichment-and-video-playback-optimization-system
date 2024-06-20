import mysql.connector
from os import getenv
from flask import Flask, request, render_template

app = Flask(__name__)

h = ''   # Fill in host name
db = ''   # Fill in db name
usr = ''   # Fill in username
pw = ''   # Fill in password

def get_movie_metadata(title):
    try:
        connection = mysql.connector.connect(
            host=h,
            database=db,
            user=usr,
            password=pw
        )
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM movies WHERE title = %s"
        cursor.execute(query, (title,))
        result = cursor.fetchone()
        app.logger.debug(f"Query result: {result}")
        return result
    except mysql.connector.Error as err:
        app.logger.error(f"Error: {err}")
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    title = request.form['title']
    app.logger.debug(f'Searching for movie metadata with title: {title}')
    metadata = get_movie_metadata(title)
    return render_template('result.html', metadata=metadata)

def test_db_connection():
    try:
        connection = mysql.connector.connect(
            host=getenv(h),
            database=getenv(db),
            user=getenv(usr),
            password=getenv(pw)
        )
        if connection.is_connected():
            print("Connected to the database")
            cursor = connection.cursor()
            cursor.execute("SHOW TABLES")
            for table in cursor.fetchall():
                print(table)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
    
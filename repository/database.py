import psycopg2
from psycopg2.extras import RealDictCursor
from config.sql_config import SQL_URI

def get_db_connection():
    return psycopg2.connect(SQL_URI, cursor_factory=RealDictCursor)

def create_tables():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS fighters (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        martial_art VARCHAR(100) NOT NULL,
        level VARCHAR(50) NOT NULL
    )
    ''')
    connection.commit()
    cursor.close()
    connection.close()
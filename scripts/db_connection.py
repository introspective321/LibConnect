import mysql.connector
from mysql.connector import Error
import configparser

def get_connection():
    """Establish a connection to the MySQL database."""
    config = configparser.ConfigParser()
    config.read('../config/config.ini')

    try:
        conn = mysql.connector.connect(
            host=config['DATABASE']['DB_HOST'],
            port=int(config['DATABASE']['DB_PORT']),
            user=config['DATABASE']['DB_USER'],
            password=config['DATABASE']['DB_PASSWORD'],
            database=config['DATABASE']['DB_NAME']
        )
        return conn
    except Error as e:
        print(f"Error: {e}")
        return None
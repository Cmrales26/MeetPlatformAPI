import psycopg2
from dotenv import load_dotenv
import os

load_dotenv(".env")


try:
    connection = psycopg2.connect(
        host=os.getenv("DBHOST", "localhost"),
        user=os.getenv("DBUSER", "postgres"),
        password=os.getenv("DBPASS", "root"),
        database=os.getenv("DB", "meetUp"),
    )
except Exception as ex:
    print(ex)

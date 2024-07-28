import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv('HOST')
DBNAME = os.getenv('DBNAME')
USER = os.getenv('USER')
PASSWORD = os.getenv('DB_PASSWORD')

conn = psycopg2.connect(host=HOST, dbname=DBNAME, user=USER, password=PASSWORD)
cur = conn.cursor()


try:
    conn = psycopg2.connect(host=HOST, dbname=DBNAME, user=USER, password=PASSWORD)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS UserData(
            user_id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email_id VARCHAR(255) NOT NULL,
            contact_number BIGINT NOT NULL,
            password VARCHAR(255) NOT NULL
        )
    """)

    conn.commit()
    print("Table created successfully.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    if cur:
        cur.close()
    if conn:
        conn.close()
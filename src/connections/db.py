import psycopg2
import logging
import pandas as pd

from utils.credentials_management import get_database_credentials

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')


class DB:
    def __init__(self):
        credentials = get_database_credentials()
        self.dbname = credentials['dbname']
        self.user = credentials['user']
        self.password = credentials['password']
        self.host = credentials['host']
        self.port = credentials['port']
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                host=self.host,
                port=self.port,
                dbname=self.dbname,
                user=self.user,
                password=self.password
            )
            self.cursor = self.conn.cursor()
            logging.info("✔ Connected to database")
        except Exception as e:
            logging.error(f"✖ Error connecting to database: {e}")
            raise

    def close(self):
        if self.cursor:
            self.cursor.close()
            logging.info("✔ Cursor closed")
        if self.conn:
            self.conn.close()
            logging.info("✔ Connection closed")

    def execute(self, query_path, fetch_results=True):
        try:
            with open(query_path, 'r') as file:
                query = file.read()
            self.connect()
            self.cursor.execute(query)
            self.conn.commit()
            logging.info("✔ Query executed")

            # Fetch results if requested
            if fetch_results:
                return self.cursor.fetchall()
            return None
        except Exception as e:
            logging.error(f"✖ Error executing query: {e}")
            self.conn.rollback()
            raise
        finally:
            self.close()

    def fetch_as_dataframe(self, query_path):
        try:
            with open(query_path, 'r') as file:
                query = file.read()
            self.connect()
            self.cursor.execute(query)
            rows = self.cursor.fetchall()  # Get query data
            colnames = [desc[0] for desc in self.cursor.description] # Get column names
            df = pd.DataFrame(rows, columns=colnames) # Convert to df
            logging.info("✔ Data loaded into DataFrame")
            return df
        except Exception as e:
            logging.error(f"✖ Error loading data into DataFrame: {e}")
            raise
        finally:
            self.close()

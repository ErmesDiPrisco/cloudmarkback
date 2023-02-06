import mysql.connector as mysql
import json

from pathlib import Path

class Mysql:
    @classmethod
    def openconnection(cls):
        config = json.loads(Path(r'dao/utilities/config.json').read_text())
        try:
            cls.conn =  mysql.connect(**config)
            cls.cursor = cls.conn.cursor(dictionary=True)
        except mysql.Error as er:
            print("Connessione fallita...")
        finally:
            return cls.conn.cursor()

    @classmethod
    def query(cls, string):
        cls.cursor.execute(string)

    @classmethod
    def get_results(cls):
        return cls.cursor.fetchall()
    @classmethod
    def get_result(cls):
        return cls.cursor.fetchone()
    @classmethod
    def close_connection(cls):
        cls.cursor.close()
        cls.conn.close()
    
    @classmethod
    def commit(cls):
        cls.conn.commit()
import mysql.connector

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "password",
            database = "Inventory_Store",
        )
        self.cursor = self.conn.cursor()
    def execute_q(self, query, params=None):
        self.cursor.excute(query, params)
        self.conn.commit()

    def fetch_q(self, query, params=None):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()
    
    def close_q(self):
        self.cursor.close()
        self.conn.close()

